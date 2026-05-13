"""Module 5 sample 04 — str.replace(old, new, count=-1).

`count` limits how many non-overlapping replacements run; default replaces all.

Run: python src/Working/module5/04_sample.py
"""

from __future__ import annotations


def main() -> None:
    name = "j-o-s-e-p-h"
    print(f"name = {name!r}")
    print("replace('-', '') once (preview, name unchanged) ->", repr(name.replace("-", "")))
    name = name.replace("-", "")
    print("after name = name.replace('-', '')            ->", repr(name))

    university = "h-ar-w-a-r-d"
    print(f"\nuniversity = {university!r}")
    print("replace('-', '', 2)  (only first two hyphens) ->", repr(university.replace("-", "", 2)))
    print("replace('-', '')   (all hyphens)             ->", repr(university.replace("-", "")))

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
