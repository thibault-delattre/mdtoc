# mdtoc

A tiny zero-dependency CLI that generates a Markdown table of contents from a file's headers.

## Usage

```bash
python mdtoc.py README.md
```

Output:

```markdown
- [mdtoc](#mdtoc)
  - [Usage](#usage)
  - [Why](#why)
  - [Development](#development)
```

Paste the output at the top of your file, or pipe it straight into a `TOC` section.

## Why

Writing a table of contents by hand for a long README is tedious and it drifts out of sync
as headers change. `mdtoc` reads the file, skips fenced code blocks so headers inside examples
aren't picked up, and prints GitHub-style anchor links.

## Development

```bash
pip install pytest
pytest
```
