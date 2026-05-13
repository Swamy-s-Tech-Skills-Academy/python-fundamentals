"""Working draft: case helpers: swapcase, capitalize, upper, lower, title.

Run: python src/Working/module5/05_sample.py
"""

from __future__ import annotations


def main() -> None:
    sentence = "i enjoy learning python"
    print(f"original: {sentence!r}\n")

    print("swapcase()   ->", repr(sentence.swapcase()))
    print("capitalize() ->", repr(sentence.capitalize()))
    print("upper()      ->", repr(sentence.upper()))
    print("lower()      ->", repr(sentence.lower()))
    print("title()      ->", repr(sentence.title()))
    print("title().swapcase() ->", repr(sentence.title().swapcase()))

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
