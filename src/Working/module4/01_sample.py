"""Boolean logical expressions — and, or, not, precedence, truthy/falsy, short-circuit."""

# Filename: src/Working/module4/01_sample.py

import sys

HELP_TEXT = """01_sample.py

Purpose
    Explore Python Boolean logical expressions: and, or, not operators,
    operator precedence, non-bool values, falsy values, and short-circuit evaluation.

Usage
    python 01_sample.py
"""


def demo_basic_operators() -> None:
    print("=" * 50)
    print("1. BASIC BOOLEAN OPERATORS")
    print("=" * 50)

    # and: True only when BOTH operands are True
    print("\n-- and operator --")
    print(f"True  and True  => {True and True}")
    print(f"True  and False => {True and False}")
    print(f"False and True  => {False and True}")
    print(f"False and False => {False and False}")

    # or: True when at least ONE operand is True
    print("\n-- or operator --")
    print(f"True  or True  => {True or True}")
    print(f"True  or False => {True or False}")
    print(f"False or True  => {False or True}")
    print(f"False or False => {False or False}")

    # not: reverses the value
    print("\n-- not operator --")
    print(f"not True  => {not True}")
    print(f"not False => {not False}")


def demo_operator_precedence() -> None:
    print("\n" + "=" * 50)
    print("2. OPERATOR PRECEDENCE  ( () > not > and > or )")
    print("=" * 50)

    # Step-by-step: True and not True
    # not True  => False
    # True and False => False
    result1 = True and not True
    print(f"\nTrue and not True")
    print(f"  not True        => False")
    print(f"  True and False  => {result1}")

    # Step-by-step: True and False or not False or False
    # not False => True
    # True and False => False
    # False or True => True
    # True or False => True
    result2 = True and False or not False or False
    print(f"\nTrue and False or not False or False")
    print(f"  not False               => True")
    print(f"  True and False          => False")
    print(f"  False or True           => True")
    print(f"  True or False           => {result2}")

    # Parentheses override default precedence
    result3 = (True or False) and (not True or False)
    print(f"\n(True or False) and (not True or False) => {result3}")


def demo_non_bool_values() -> None:
    print("\n" + "=" * 50)
    print("3. NON-BOOL VALUES WITH BOOLEAN OPERATORS")
    print("=" * 50)

    # With and/or Python may return the actual value, not True/False
    print(f"\n1 and 0          => {1 and 0}   (int 0 = falsy; and returns first falsy)")
    print(f"not 1            => {not 1}  (not always returns a bool)")
    print(f"not 0            => {not 0}   (not always returns a bool)")

    print(f'\n1 and "loop" and "list"  => {1 and "loop" and "list"}')
    print("  (all truthy => returns rightmost value)")

    print(f'\n"" and "loop" and "list" and []  => {repr("" and "loop" and "list" and [])}')
    print('  (empty string is falsy => returns first falsy: "")')


def demo_falsy_values() -> None:
    print("\n" + "=" * 50)
    print("4. FALSY VALUES IN PYTHON")
    print("=" * 50)

    falsy_candidates = [None, 0, 0.0, "", [], (), {}]
    for val in falsy_candidates:
        print(f"  bool({repr(val):<8}) => {bool(val)}")

    print("\n  Everything else is truthy (non-zero numbers, non-empty strings/collections).")


def demo_short_circuit() -> None:
    print("\n" + "=" * 50)
    print("5. SHORT-CIRCUIT EVALUATION")
    print("=" * 50)

    # and returns first falsy value, or last value if all truthy
    print("\n-- and short-circuit --")
    print(f'  0 and "skip"   => {repr(0 and "skip")}   (stops at 0; never checks "skip")')
    print(f'  1 and "keep"   => {repr(1 and "keep")}  (1 truthy; returns last value)')

    # or returns first truthy value, or last value if all falsy
    print("\n-- or short-circuit --")
    print(f'  0 or "found"   => {repr(0 or "found")}  (0 falsy; keeps looking; returns "found")')
    print(f'  1 or "ignore"  => {repr(1 or "ignore")}      (1 truthy; stops immediately)')

    print("\n  Tip: short-circuit evaluation powers many Python idioms, e.g.:")
    print('       name = user_input or "Guest"')


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_basic_operators()
    demo_operator_precedence()
    demo_non_bool_values()
    demo_falsy_values()
    demo_short_circuit()

    print("\n" + "=" * 50)
    print("Done. Experiment: change values and predict outputs before running!")
    print("=" * 50)
    return 0


raise SystemExit(main(sys.argv))
