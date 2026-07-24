from mdtoc import build_toc, extract_headers, slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_chars():
    assert slugify("Getting Started: Step 1!") == "getting-started-step-1"


def test_extract_headers_ignores_code_blocks():
    lines = [
        "# Title\n",
        "```\n",
        "# not a header\n",
        "```\n",
        "## Section\n",
    ]
    assert extract_headers(lines) == [(1, "Title"), (2, "Section")]


def test_build_toc_nesting():
    headers = [(1, "Intro"), (2, "Sub Section")]
    toc = build_toc(headers)
    assert toc == "- [Intro](#intro)\n  - [Sub Section](#sub-section)"


def test_build_toc_empty():
    assert build_toc([]) == ""
