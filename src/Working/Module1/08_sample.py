"""Day 8: Escape sequences in strings.

Builds on Day 7: end='' can join lines; inside a string, \\n and \\t do similar
formatting work. You also escape quotes so Python does not end the string early.

This is the last numbered day in this Module1 chain; polish here, then promote
into formal src/L1/S... files when your session outline is ready.
"""

# Filename: src/Working/Module1/08_sample.py

import sys

HELP_TEXT = """08_sample.py

Purpose
    Practice escape sequences for formatting and special characters.

Usage
    python 08_sample.py

Topics Covered
    - New line: \\n
    - Tab space: \\t
    - Backspace effect: \\b
    - Escaping quotes inside strings

This wraps the Module1 sandbox thread on formatted text output.
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("Day 8: Backslash starts an escape - it changes how the string prints.\n")

    print("=== New line (\\n) ===")
    print("My name is Joseph\nI'm 29 years old")

    print("\n=== Tab (\\t) ===")
    print("My name is Joseph\tI'm 29 years old")
    print("My name is Joseph\t\tI'm 29 years old")

    print("\n=== Backspace (\\b) ===")
    print("My name is Joseph\bI'm 29 years old")

    print("\n=== Escaping apostrophe ===")
    print("Using double quotes:", "I'm 29 years old")
    print("Using escape in single quotes:", 'I\'m 29 years old')

    return 0


raise SystemExit(main(sys.argv))