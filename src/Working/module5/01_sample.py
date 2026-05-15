"""Working draft: strings, comments, type(), +, *, and TypeError demos."""

# Filename: src/Working/module5/01_sample.py

import sys

HELP_TEXT = """01_sample.py

Purpose
    Explore basic string rules: quoting, comments, type(), concatenation,
    repetition, and a few invalid operations that raise TypeError.

Usage
    python src/Working/module5/01_sample.py
"""


def show_type_error(label: str, fn) -> None:
    print(f"\n--- {label} ---")
    try:
        fn()
    except TypeError as exc:
        print(f"TypeError (expected): {exc}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

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
    return 0


raise SystemExit(main(sys.argv))
