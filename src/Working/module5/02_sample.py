"""Working draft: len() on strings (spaces count as characters)."""

import sys

HELP_TEXT = """02_sample.py

Purpose
    Show that len() counts every character in a string, including spaces.

Usage
    python src/Working/module5/02_sample.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    title = "python coach"
    n = len(title)
    print(f"title = {title!r}")
    print(f"len(title) = {n}")
    print("Spaces inside the string count toward the length.")

    print()
    print(f'len("")         -> {len("")}')
    print(f'len("python")   -> {len("python")}')
    print(f'len("hi there") -> {len("hi there")}")
    return 0


raise SystemExit(main(sys.argv))
