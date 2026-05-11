"""Day 1: Hello World (Printing)

This file is intentionally simple for beginners.

What you practice here:
- Running a Python file from the terminal
- Using the built-in `print()` function
- Writing strings with different quote styles (double quotes, single quotes, and triple-quoted strings)

Why we need single quotes, double quotes, and triple quotes:
- `'...'` and `"..."` both create normal one-line strings.
- We choose one or the other to reduce escaping and improve readability.
    Example: use `"It's my pleasure"` to avoid escaping the apostrophe.
    Example: use `'He said "Hello"'` to avoid escaping outer double quotes.
- Triple quotes are best for multi-line text and docstrings.
    It keeps blocks like help text, banners, and explanations easy to read.

Try it:
- Run: `python 01_sample.py`
- Help: `python 01_sample.py --help`

Next idea:
- Once printing feels easy, compare `02_sample.py` (values, types, and variables).
"""

# Filename: src/Working/Module1/01_sample.py

import sys

HELP_TEXT = """01_sample.py

Purpose
    Practice printing text to the screen.

Usage
    python 01_sample.py

Notes
    - Edit the messages and run again to see changes.
    - The examples show different ways to write string literals.
    - `'...'` and `"..."` are one-line strings; choose what avoids escaping.
    - Triple quotes are useful for multi-line strings and documentation.

Next script
    02_sample.py - store values in variables and ask what type they are.
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("Day 1: Printing is your first feedback loop - you see what Python evaluated.\n")

    print("=== Basic print() examples ===")
    print("Hello Data Science")
    print("Hello Friends")
    print("Hello Data Science")
    print("Hello Data Science")
    print("""Hello Data Science""")

    print(
        'the name of the python programming language does not come from "python snake"'
    )

    print("\n=== Quote style examples ===")
    print("It's my pleasure")
    print("""It's my pleasure""")

    print("\n=== Multi-line banner (triple quotes) ===")
    print("""
[H]=========ALICVDR=======[-][o][x]
|                                 |
|       Welcome to program!       |
|           version 5             |                          
|     Tap anywhere to continue    |
|                                 |
|=================================| """)

    return 0


raise SystemExit(main(sys.argv))
