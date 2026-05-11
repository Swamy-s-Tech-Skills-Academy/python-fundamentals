"""Compound conditions for loops: and, or, not, and evaluation order.

Pairs with Session 6 while-loops: messy headers are a common source of
"why does my loop never run?" bugs. Use parentheses when in doubt.
"""

from __future__ import annotations


def main() -> None:
    print("=== 1) Truth tables (quick reminders) ===")
    print("True and False ->", True and False)
    print("True or False  ->", True or False)
    print("not False        ->", not False)

    print("\n=== 2) Order without parentheses: not, then and, then or ===")
    # Same rule as arithmetic: use explicit () when readers might pause.
    expr = True and not False or False
    print("True and not False or False  =>", expr)
    print("  (parsed as: (True and (not False)) or False)")

    explicit = (True and (not False)) or False
    print("explicit form                =>", explicit)

    print("\n=== 3) Parentheses win - always ===")
    changed = True or (False and False)
    print("True or (False and False) =>", changed)

    print("\n=== 4) Tiny while-loop: compound condition ===")
    count = 0
    # Run while count is small AND we have not hit the cap on evens printed.
    evens_printed = 0
    while count < 8 and evens_printed < 3:
        if count % 2 == 0:
            print(f"  even: {count}")
            evens_printed += 1
        count += 1
    print("Loop exited because one side of `and` became false.")

    print("\n=== Done ===")
    print("Experiment: wrap parts of a messy condition in () and predict the result before running.")


if __name__ == "__main__":
    main()
