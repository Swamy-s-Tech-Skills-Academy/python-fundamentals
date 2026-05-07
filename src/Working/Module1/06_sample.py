"""Day 6: Arithmetic operators in Python."""

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
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Arithmetic operators ===")
    print("29 % 7 =", 29 % 7)
    print("9 // 2 =", 9 // 2)
    print("2 ** 3 =", 2**3)

    print("\n=== Even/Odd quick check using modulo ===")
    number = 10
    print(f"{number} % 2 =", number % 2)
    print("If result is 0, the number is even.")

    print("\n=== Reassigning with arithmetic ===")
    x = 5
    x = x + 5
    print("After x = x + 5, x =", x)

    x = 15
    x += 10
    print("After x += 10, x =", x)

    print("\n=== Expression priority example ===")
    a = (2 + 5) ** (2 ** (1 * 4 / 4) / 2)
    print("a =", a)

    return 0


raise SystemExit(main(sys.argv))
