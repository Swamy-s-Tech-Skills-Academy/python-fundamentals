"""Working draft: str.replace(old, new, count=-1)."""

# Filename: src/Working/module5/04_sample.py

import sys

HELP_TEXT = """04_sample.py

Purpose
    Show how replace() swaps text and how the optional count argument limits
    how many replacements happen.

Usage
    python src/Working/module5/04_sample.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    code_word = "p-y-t-h-o-n"
    print(f"code_word = {code_word!r}")
    print(
        "replace('-', '') once (preview, word unchanged) ->",
        repr(code_word.replace("-", "")),
    )
    code_word = code_word.replace("-", "")
    print("after code_word = code_word.replace('-', '')  ->", repr(code_word))

    course_name = "b-e-g-i-n-n-e-r"
    print(f"\ncourse_name = {course_name!r}")
    print(
        "replace('-', '', 2)  (only first two hyphens) ->",
        repr(course_name.replace("-", "", 2)),
    )
    print(
        "replace('-', '')   (all hyphens)             ->",
        repr(course_name.replace("-", "")),
    )

    print("\n=== Done ===")
    return 0


raise SystemExit(main(sys.argv))
