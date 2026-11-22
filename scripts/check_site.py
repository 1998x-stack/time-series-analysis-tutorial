#!/usr/bin/env python3
"""No-dependency static site checks; not a substitute for browser QA."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.h1 = 0
        self.maths = 0
        self.figures = 0
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if attr.get('id'):
            self.ids.add(attr['id'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'math':
            self.maths += 1
        if tag == 'figure':
            self.figures += 1
        for key in ('href', 'src'):
            if key in attr:
                self.links.append(attr[key])

def fail(msg):
    print('FAIL:', msg)
    return 1

def main():
    errors = 0
    data = json.loads((ROOT/'courses.json').read_text(encoding='utf-8'))
    chapters = data['chapters']
    if len(chapters) != 28 or [c['num'] for c in chapters] != [f'{i:02d}' for i in range(1,29)]:
        errors += fail('catalog must contain 01..28 in order')
    fresh = [ROOT/'index.html'] + [ROOT/f'chapters/{i:02d}.html' for i in range(1,6)]
    for page in fresh:
        if not page.is_file():
            errors += fail(f'missing {page.relative_to(ROOT)}')
            continue
        contents = page.read_text(encoding='utf-8')
        parser = Links(); parser.feed(contents)
        expected = 0 if page.name == 'index.html' else 1
        if parser.h1 != 1:
            errors += fail(f'{page.name}: expected 1 h1, got {parser.h1}')
        if expected and (parser.figures < 2 or parser.maths < 2):
            errors += fail(f'{page.name}: expected >=2 figures and math blocks')
        if 'javascript:void' in contents or '大家好，我是你们的讲师' in contents:
            errors += fail(f'{page.name}: forbidden process/placeholder prose')
        for url in parser.links:
            if url.startswith(('http://','https://','mailto:','data:')):
                continue
            if url.startswith(('javascript:','//')):
                errors += fail(f'{page.name}: forbidden link {url}')
                continue
            parsed = urlsplit(url)
            if not parsed.path:
                if parsed.fragment and parsed.fragment not in parser.ids:
                    errors += fail(f'{page.name}: missing fragment {parsed.fragment}')
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
                errors += fail(f'{page.relative_to(ROOT)}: broken local link {url}')
    for item in chapters:
        if not (ROOT/item['file']).is_file():
            errors += fail(f'missing canonical chapter {item["file"]}')
        old = ROOT/f'{item["num"]}.html'
        if not old.is_file() or item['file'] not in old.read_text(encoding='utf-8'):
            errors += fail(f'broken legacy redirect {old.name}')
    for f in sorted((ROOT/'assets/svg').glob('*.svg')):
        try:
            tree = ET.parse(f)
            top = tree.getroot()
            namespace = '{http://www.w3.org/2000/svg}'
            if top.tag != namespace + 'svg' or 'viewBox' not in top.attrib:
                errors += fail(f'{f.name}: root/svg viewBox')
            if top.find(namespace+'title') is None or top.find(namespace+'desc') is None:
                errors += fail(f'{f.name}: missing title/desc')
        except ET.ParseError as e:
            errors += fail(f'{f.name}: bad XML: {e}')
    if len(list((ROOT/'assets/svg').glob('*.svg'))) < 10:
        errors += fail('expected at least 10 dedicated SVG diagrams')
    print(f'Checked {len(fresh)} core pages, {len(chapters)} chapters, SVG files: {len(list((ROOT/"assets/svg").glob("*.svg")))}')
    return int(errors != 0)

if __name__ == '__main__':
    sys.exit(main())
