#!/usr/bin/env python3
"""Extract and execute chapter <pre><code> examples separately in new Python processes."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
class Snippets(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pre = 0
        self.code = 0
        self.current = []
        self.samples = []
    def handle_starttag(self, tag, attrs):
        if tag == "pre": self.pre += 1
        if tag == "code" and self.pre:
            self.code += 1
            self.current = []
    def handle_data(self, data):
        if self.code: self.current.append(data)
    def handle_endtag(self, tag):
        if tag == "code" and self.code:
            self.code -= 1
            self.samples.append("".join(self.current).strip())
        if tag == "pre" and self.pre: self.pre -= 1

def main():
    count = 0
    for number in range(1, 11):
        article = ROOT / f"chapters/{number:02d}.html"
        parser = Snippets()
        parser.feed(article.read_text(encoding="utf-8"))
        if not parser.samples:
            raise RuntimeError(f"{article.name}: missing executable example")
        for idx, sample in enumerate(parser.samples, 1):
            print(f"RUN {article.name} code #{idx}", flush=True)
            run = subprocess.run([sys.executable, "-c", sample], cwd=ROOT,
                                 capture_output=True, text=True, timeout=90)
            if run.returncode:
                print(run.stdout)
                print(run.stderr)
                raise RuntimeError(f"{article.name}: example {idx} did not pass")
            count += 1
    print(f"PASS {count} isolated Python examples across 01–10")

if __name__ == "__main__":
    main()
