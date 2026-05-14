"""Day 7: print() with sep and end.

Builds on Day 1: plain print(items) prints each piece with spaces and ends with a
new line by default. This file tweaks those defaults for cleaner output.
"""

# Filename: src/Working/module3/07_sample.py

import sys

HELP_TEXT = """07_sample.py

Purpose
    Understand how print() handles multiple values, separators, and line endings.

Usage
    python src/Working/module3/07_sample.py

Topics Covered
    - Printing multiple values with commas
    - sep to change what goes between pieces
    - end to suppress or extend the trailing newline

Next script
    src/Working/module3/08_sample.py - escapes inside strings (including \\n in text).
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("Day 7: print can join values and choose what happens after the line.\n")

    lesson_number = 7
    sentence = "Current lesson"

    print("=== Multiple values in print() ===")
    print(sentence, lesson_number)

    print("\n=== Using sep ===")
    print(sentence, lesson_number, sep="-")
    print(sentence, lesson_number, sep=" | ")

    print("\n=== Using end ===")
    print(sentence, lesson_number, sep="-", end="  <-- same line ->  ")
    print(sentence, lesson_number, sep="-")

    print("\n=== Common beginner mistake ===")
    print("Wrong:  print(sentence lesson_number)")
    print("Right:  print(sentence, lesson_number)")

    return 0


raise SystemExit(main(sys.argv))
