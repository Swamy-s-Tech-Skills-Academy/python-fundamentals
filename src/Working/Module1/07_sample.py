"""Day 7: Exploring print() arguments in depth."""

# Filename: src/Working/Module1/07_sample.py

import sys

HELP_TEXT = """07_sample.py

Purpose
    Understand how print() handles multiple values, separators, and line endings.

Usage
    python 07_sample.py

Topics Covered
    - Printing multiple values with commas
    - Using sep to customize separators
    - Using end to control line breaks
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

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