"""Day 6: Arithmetic operators.

Builds on Day 2 and Day 5: you already combine ints and floats. Here you meet
modulo, floor division, powers, shorthand +=, and a compact precedence puzzle.
"""

# Filename: src/Working/Module1/06_sample.py

import sys

HELP_TEXT = """06_sample.py

Purpose
    Practice arithmetic operators and expression priority in Python.

Usage
    python 06_sample.py

Topics Covered
    - Modulo (%): remainder after division
    - Floor division (//): integer part of a division
    - Exponentiation (**): power operation
    - Compound assignment (+=)
    - Operator priority in expressions

Next script
    07_sample.py - control spacing and line breaks inside print().
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print(
        "Day 6: Build on Days 2 and 5 - combine numbers with %, //, **, and +=.\n"
    )

    print("=== Arithmetic operators ===")
    print("29 % 7 =", 29 % 7)
    print("9 // 2 =", 9 // 2)
    print("2 ** 3 =", 2**3)

    print("\n=== Even/Odd quick check using modulo ===")
    number = 10
    print(f"{number} % 2 =", number % 2)
    print("If n % 2 is 0, n is even; if it is 1, n is odd (for whole numbers).")

    print("\n=== Reassigning with arithmetic ===")
    x = 5
    x = x + 5
    print("After x = x + 5, x =", x)

    x = 15
    x += 10
    print("After x += 10, x =", x)

    print("\n=== Expression precedence (inner parens first) ===")
    a = (2 + 5) ** (2 ** (1 * 4 / 4) / 2)
    print("a =", a)

    return 0


raise SystemExit(main(sys.argv))
