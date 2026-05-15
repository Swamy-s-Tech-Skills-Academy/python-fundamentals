"""Working draft: strip(), lstrip(), and rstrip()."""

# Filename: src/Working/module5/06_sample.py

import sys

HELP_TEXT = """06_sample.py

Purpose
    Demonstrate how strip(), lstrip(), and rstrip() remove whitespace or
    chosen leading and trailing characters.

Usage
    python src/Working/module5/06_sample.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    padded_text = "   practice   "
    print(f"padded_text = {padded_text!r}\n")

    print("strip()   ->", repr(padded_text.strip()))
    print("rstrip()  ->", repr(padded_text.rstrip()))
    print("lstrip()  ->", repr(padded_text.lstrip()))

    inner = padded_text.strip()
    print(f"\nAfter strip: {inner!r}")
    print('strip("e") removes leading/trailing e from that result ->', repr(inner.strip("e")))

    print("\nTip: help(str.strip) in the REPL explains the optional chars argument.")

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
