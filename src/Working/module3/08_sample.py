"""Day 8: Escape sequences in strings.

Builds on Day 7: end='' can join lines; inside a string, \\n and \\t do similar
formatting work. You also escape quotes so Python does not end the string early.

This is the last numbered day in this module3 chain; polish here, then promote
into formal src/L1/S... files when your session outline is ready.
"""

# Filename: src/Working/module3/08_sample.py

import sys

HELP_TEXT = """08_sample.py

Purpose
    Practice escape sequences for formatting and special characters.

Usage
    python src/Working/module3/08_sample.py

Topics Covered
    - New line: \\n
    - Tab space: \\t
    - Backspace effect: \\b
    - Escaping quotes inside strings

This wraps the module3 sandbox thread on formatted text output.
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("Day 8: Backslash starts an escape - it changes how the string prints.\n")

    print("=== New line (\\n) ===")
    print("Course: Python Fundamentals\nTrack: Beginner Practice")

    print("\n=== Tab (\\t) ===")
    print("Name:\tPython Fundamentals")
    print("Level:\t\tBeginner")

    print("\n=== Backspace (\\b) ===")
    print("Plan A\bB")

    print("\n=== Escaping apostrophe ===")
    print("Using double quotes:", "I'm building Python skills")
    print('Using escape in single quotes:', 'I\'m building Python skills')

    return 0


raise SystemExit(main(sys.argv))
