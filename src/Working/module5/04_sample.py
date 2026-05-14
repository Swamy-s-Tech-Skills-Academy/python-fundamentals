"""Working draft: str.replace(old, new, count=-1).

`count` limits how many non-overlapping replacements run; default replaces all.

Run: python src/Working/module5/04_sample.py
"""

from __future__ import annotations


def main() -> None:
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


if __name__ == "__main__":
    main()
