#!/usr/bin/env python3
"""Generate a table of contents from Markdown headers."""

import argparse
import re
import sys

HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)")


def slugify(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    return slug


def extract_headers(lines: list[str]) -> list[tuple[int, str]]:
    headers = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        match = HEADER_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append((level, title))
    return headers


def build_toc(headers: list[tuple[int, str]]) -> str:
    if not headers:
        return ""
    min_level = min(level for level, _ in headers)
    lines = []
    for level, title in headers:
        indent = "  " * (level - min_level)
        slug = slugify(title)
        lines.append(f"{indent}- [{title}](#{slug})")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown table of contents from headers.")
    parser.add_argument("file", help="Path to the Markdown file")
    args = parser.parse_args(argv)

    with open(args.file, encoding="utf-8") as f:
        lines = f.readlines()

    headers = extract_headers(lines)
    toc = build_toc(headers)
    if toc:
        print(toc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
