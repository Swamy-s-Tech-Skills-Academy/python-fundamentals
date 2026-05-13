"""Working draft: strings, comments, type(), +, *, and TypeError demos.

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
    print("A bare phrase like practice time is a SyntaxError in code; use quotes or # for notes.")
    # hello world  (this line is a comment — Python ignores it)

    print("\n=== Numeric literal vs numeric text ===")
    print("type(987)        ->", type(987))
    print('type("987")      ->', type("987"))

    print("\n=== String concatenation (+) ===")
    print('"python" + "class"     ->', repr("python" + "class"))
    print('"python" + " class"    ->', repr("python" + " class"))
    print('"python" + " " + "class" ->', repr("python" + " " + "class"))

    show_type_error("Minus between strings (not supported)", lambda: "python" - " class")

    print("\n=== Repetition with * (int times str) ===")
    print('"go" * 3      ->', repr("go" * 3))

    show_type_error("Multiply str * str (invalid)", lambda: "go" * "go")
    show_type_error("Divide str / int", lambda: "go" / 3)

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
