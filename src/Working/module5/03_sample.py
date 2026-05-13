"""Working draft: str.startswith / str.endswith and optional start, end slices.

Run: python src/Working/module5/03_sample.py
"""

from __future__ import annotations


def main() -> None:
    web_address = "www.learnpython.dev"

    print(f"web_address = {web_address!r}\n")

    print("startswith('www')     ->", web_address.startswith("www"))
    print("startswith('com')     ->", web_address.startswith("com"))
    print("endswith('.dev')      ->", web_address.endswith(".dev"))

    # Between start (inclusive) and end (exclusive): s[start:end] must start with prefix.
    print("startswith('learn', 4, 12) ->", web_address.startswith("learn", 4, 12))

    # endswith also accepts start/end bounds on the substring window (end is exclusive).
    print("endswith('python', 4, 15)   ->", web_address.endswith("python", 4, 15))

    print("\nTip: in the REPL, type web_address.startswith( then Shift+Tab to read the docstring.")


if __name__ == "__main__":
    main()
