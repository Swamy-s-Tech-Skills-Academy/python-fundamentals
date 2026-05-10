"""Day 7: print() with sep and end.

Builds on Day 1: plain print(items) prints each piece with spaces and ends with a
new line by default. This file tweaks those defaults for cleaner output.
"""

# Filename: src/Working/Module1/07_sample.py

import sys

HELP_TEXT = """07_sample.py

Purpose
    Understand how print() handles multiple values, separators, and line endings.

Usage
    python 07_sample.py

Topics Covered
    - Printing multiple values with commas
    - sep to change what goes between pieces
    - end to suppress or extend the trailing newline

Next script
    08_sample.py - escapes inside strings (including \\n in text).
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print(
        "Day 7: print can join values and choose what happens after the line.\n"
    )

    age = 29
    sentence = "My age is"

    print("=== Multiple values in print() ===")
    print(sentence, age)

    print("\n=== Using sep ===")
    print(sentence, age, sep="-")
    print(sentence, age, sep=" | ")

    print("\n=== Using end ===")
    print(sentence, age, sep="-", end="  <-- same line ->  ")
    print(sentence, age, sep="-")

    print("\n=== Common beginner mistake ===")
    print("Wrong:  print(sentence age)")
    print("Right:  print(sentence, age)")

    return 0


raise SystemExit(main(sys.argv))