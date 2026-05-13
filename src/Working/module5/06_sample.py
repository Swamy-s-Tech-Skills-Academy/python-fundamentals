"""Working draft: strip, rstrip, lstrip (trim spaces or custom chars).

Run: python src/Working/module5/06_sample.py
"""

from __future__ import annotations


def main() -> None:
    padded_text = "   practice   "
    print(f"padded_text = {padded_text!r}\n")

    print("strip()   ->", repr(padded_text.strip()))
    print("rstrip()  ->", repr(padded_text.rstrip()))
    print("lstrip()  ->", repr(padded_text.lstrip()))

    inner = padded_text.strip()
    print(f"\nAfter strip: {inner!r}")
    print('strip("e") removes leading/trailing e from that result ->', repr(inner.strip("e")))

    print("\nTip: help(str.strip) in the REPL explains the optional chars argument.")

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
