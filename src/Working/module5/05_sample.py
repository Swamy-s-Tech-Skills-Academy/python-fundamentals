"""Working draft: case helpers: swapcase, capitalize, upper, lower, title."""

import sys

HELP_TEXT = """05_sample.py

Purpose
    Compare common string case-conversion helpers and see how each one changes
    the same sentence.

Usage
    python src/Working/module5/05_sample.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    sentence = "i enjoy learning python"
    print(f"original: {sentence!r}\n")

    print("swapcase()   ->", repr(sentence.swapcase()))
    print("capitalize() ->", repr(sentence.capitalize()))
    print("upper()      ->", repr(sentence.upper()))
    print("lower()      ->", repr(sentence.lower()))
    print("title()      ->", repr(sentence.title()))
    print("title().swapcase() ->", repr(sentence.title().swapcase()))

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
