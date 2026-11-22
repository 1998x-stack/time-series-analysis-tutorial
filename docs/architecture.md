# Static site architecture

## Why move the old files?

The original repository contained 28 separate top-level HTML articles and a single shared theme. This release introduces a canonical `chapters/NN.html` namespace while preserving `NN.html` public addresses as redirect pages. The original first five HTMLs, former homepage and README are kept in `archive/`; chapter 06–28 HTMLs are copied unmodified into `chapters/` and continue to use the legacy `chapters/theme.css`.

## Routes

- `/` = homepage & entire 28-chapter catalog.
- `/chapters/01.html` to `/chapters/05.html` = redesigned long-form lessons.
- `/chapters/06.html` to `/chapters/28.html` = preserved original chapters pending audit.
- `/01.html` to `/28.html` = old inbound links, redirect.
- `/chapters/index.html` = legacy relative “return to catalog” link, redirect to root.

## Rendering and deployment

GitHub Pages can serve the repository root directly because all new HTML/CSS/SVG files are committed, no bundler is needed. `.nojekyll` prevents Jekyll transformations. For Actions-based publication, `.github/workflows/pages.yml` packages the same files into a Pages artifact; repository Settings → Pages must choose “GitHub Actions” for that path to be active. The workflow does not itself prove a site is live.

## Quality scope

`scripts/check_site.py` checks links, chapter count, independent SVG XML, page semantics, formula nodes and old redirects. This is **static** validation, not a substitute for Playwright browser rendering at desktop/mobile sizes, keyboard and print inspections. See `AGENTS.md` for release gates.
