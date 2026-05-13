"""Working draft: len() on strings (spaces count as characters).

Run: python src/Working/module5/02_sample.py
"""

from __future__ import annotations


def main() -> None:
    title = "python coach"
    n = len(title)
    print(f"title = {title!r}")
    print(f"len(title) = {n}")
    print("Spaces inside the string count toward the length.")


if __name__ == "__main__":
    main()
