#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "index.html",
    "about/index.html",
    "training/index.html",
    "start/index.html",
    "404.html",
    "assets/css/site.css",
    "js/site.js",
    "favicon.svg",
    "robots.txt",
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.assets = []
        self.h1_count = 0
        self.has_title = False
        self.has_viewport = False
        self.has_main = False
        self.has_skip_link = False
        self._inside_title = False
        self._title_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if "skip-link" in attrs.get("class", "").split():
                self.has_skip_link = True
        if tag in {"script", "img", "source", "link"}:
            value = attrs.get("src") or attrs.get("href")
            if value:
                self.assets.append(value)
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.has_main = True
        if tag == "meta" and attrs.get("name") == "viewport":
            self.has_viewport = True
        if tag == "title":
            self._inside_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._inside_title = False
            self.has_title = bool("".join(self._title_text).strip())

    def handle_data(self, data):
        if self._inside_title:
            self._title_text.append(data)

def is_external(url):
    parsed = urlparse(url)
    return bool(parsed.scheme or parsed.netloc) or url.startswith(("mailto:", "tel:", "#", "data:"))

def resolve_local(page, ref):
    clean = ref.split("#", 1)[0].split("?", 1)[0]
    if not clean or is_external(clean):
        return None
    base = page.parent
    target = (base / clean).resolve()
    if not str(target).startswith(str(ROOT.resolve())):
        raise AssertionError(f"{page}: local reference escapes repository: {ref}")
    if clean.endswith("/"):
        target = target / "index.html"
    elif target.is_dir():
        target = target / "index.html"
    return target

def check_page(page):
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))

    errors = []
    if not parser.has_title:
        errors.append("missing non-empty <title>")
    if not parser.has_viewport:
        errors.append("missing viewport meta")
    if not parser.has_main:
        errors.append("missing <main>")
    if parser.h1_count != 1:
        errors.append(f"expected exactly one <h1>, found {parser.h1_count}")
    if page.name != "404.html" and not parser.has_skip_link:
        errors.append("missing skip link")

    for ref in parser.links + parser.assets:
        target = resolve_local(page, ref)
        if target and not target.exists():
            errors.append(f"broken local reference: {ref} -> {target.relative_to(ROOT)}")

    return errors

def main():
    problems = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            problems.append(f"missing required file: {rel}")

    for page in [ROOT / "index.html", ROOT / "about/index.html", ROOT / "training/index.html", ROOT / "start/index.html", ROOT / "404.html"]:
        if page.exists():
            for error in check_page(page):
                problems.append(f"{page.relative_to(ROOT)}: {error}")

    if problems:
        print("Site validation FAILED:")
        for item in problems:
            print(f" - {item}")
        raise SystemExit(1)

    print("Site validation passed.")
    print("Checked required files, page structure, and local navigation/assets.")

if __name__ == "__main__":
    main()
