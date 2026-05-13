"""Module 5 sample 06 — strip, rstrip, lstrip (trim spaces or custom chars).

Run: python src/Working/module5/06_sample.py
"""

from __future__ import annotations


def main() -> None:
    space = "   example   "
    print(f"space = {space!r}\n")

    print("strip()   ->", repr(space.strip()))
    print("rstrip()  ->", repr(space.rstrip()))
    print("lstrip()  ->", repr(space.lstrip()))

    inner = space.strip()
    print(f"\nAfter strip: {inner!r}")
    print('strip("e") removes leading/trailing e from that result ->', repr(inner.strip("e")))

    print("\nTip: help(str.strip) in the REPL explains the optional chars argument.")

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
