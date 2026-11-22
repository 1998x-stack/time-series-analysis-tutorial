#!/usr/bin/env python3
"""Playwright smoke test; run after: pip install playwright && playwright install chromium."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports" / "browser"
REPORTS.mkdir(parents=True, exist_ok=True)
PAGES = ["index.html"] + [f"chapters/{i:02d}.html" for i in range(1, 6)]
WIDTHS = [1440, 390, 360]

def main():
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for relative in PAGES:
            for width in WIDTHS:
                context = browser.new_context(viewport={"width": width, "height": 900},
                                              device_scale_factor=1)
                page = context.new_page()
                js_errors = []
                page.on("pageerror", lambda error: js_errors.append(str(error)))
                page.goto((ROOT / relative).as_uri(), wait_until="load")
                page.screenshot(path=str(REPORTS / (relative.replace("/", "_").replace(".html", "")
                                                    + f"-{width}.png")), full_page=True)
                bad = page.evaluate("""() => ({
                    overflow: document.documentElement.scrollWidth > innerWidth,
                    brokenImages: [...document.images].filter(x => !x.complete || !x.naturalWidth).map(x=>x.src),
                    hiddenMath: [...document.querySelectorAll('math')].filter(x =>
                        x.getBoundingClientRect().width === 0 ||
                        x.getBoundingClientRect().height === 0).length,
                })""")
                if bad["overflow"] or bad["brokenImages"] or bad["hiddenMath"] or js_errors:
                    failures.append((relative, width, bad, js_errors))
                if relative == "chapters/05.html":
                    slider = page.locator("#alpha")
                    slider.evaluate("""el => {
                        el.value = "0.70";
                        el.dispatchEvent(new Event("input", {bubbles:true}));
                    }""")
                    if page.locator("[data-alpha-value]").inner_text() != "0.70":
                        failures.append((relative, width, "alpha slider not reactive"))
                context.close()
        browser.close()
    if failures:
        for item in failures:
            print("FAIL:", item)
        raise SystemExit(1)
    print("Browser smoke checks passed for 6 pages × 3 widths; see reports/browser/.")

if __name__ == "__main__":
    main()
