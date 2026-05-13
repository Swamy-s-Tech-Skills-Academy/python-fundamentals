"""Module 5 sample 01 — strings: quotes, comments, type(), +, *, and TypeError demos.

Run: python src/Working/module5/01_sample.py
"""

from __future__ import annotations


def show_type_error(label: str, fn) -> None:
    print(f"\n--- {label} ---")
    try:
        fn()
    except TypeError as exc:
        print(f"TypeError (expected): {exc}")


def main() -> None:
    print("=== Quotes and comments ===")
    print('A bare phrase like hello world is a SyntaxError in code; use quotes or # for notes.')
    # hello world  (this line is a comment — Python ignores it)

    print("\n=== Numeric literal vs numeric text ===")
    print("type(987)        ->", type(987))
    print('type("987")      ->', type("987"))

    print("\n=== String concatenation (+) ===")
    print('"hello" + "data"     ->', repr("hello" + "data"))
    print('"hello" + " data"    ->', repr("hello" + " data"))
    print('"hello" + " " + "data" ->', repr("hello" + " " + "data"))

    show_type_error('Minus between strings (not supported)', lambda: "hello" - " data")

    print("\n=== Repetition with * (int times str) ===")
    print('"hello" * 3      ->', repr("hello" * 3))

    show_type_error("Multiply str * str (invalid)", lambda: "hello" * "hello")
    show_type_error("Divide str / int", lambda: "hello" / 3)

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
