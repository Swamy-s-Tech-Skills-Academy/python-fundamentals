"""Working draft: string indexing and slicing."""

# Filename: src/Working/module5/07_sample.py

import sys

HELP_TEXT = """07_sample.py

Purpose
	Demonstrate string indexing, negative indexes, basic slicing, and step
	slicing with a few predictable examples.

Usage
	python src/Working/module5/07_sample.py
"""


def show_slice(label: str, text: str, start: int | None, stop: int | None, step: int | None = None) -> None:
	print(f"{label:<28} -> {text[start:stop:step]!r}")


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	course_name = "python"
	print(f"course_name = {course_name!r}\n")

	print("Indexing examples")
	print("-" * 40)
	print(f"First character              -> {course_name[0]!r}")
	print(f"Third character              -> {course_name[2]!r}")
	print(f"Last character               -> {course_name[-1]!r}")
	print(f"Second-to-last character     -> {course_name[-2]!r}")

	print("\nSlicing examples")
	print("-" * 40)
	show_slice("Characters 1 to 4", course_name, 1, 5)
	show_slice("From index 2 onward", course_name, 2, None)
	show_slice("From start to index 4", course_name, None, 4)
	show_slice("Middle section", course_name, 1, 4)
	show_slice("Last three characters", course_name, -3, None)

	print("\nStep slicing")
	print("-" * 40)
	show_slice("Every second character", course_name, None, None, 2)
	show_slice("Reverse the string", course_name, None, None, -1)
	show_slice("Reverse every second", course_name, None, None, -2)

	print("\nRemember:")
	print("- Indexes start at 0 in Python.")
	print("- Negative indexes count back from the end.")
	print("- The start index is included in a slice.")
	print("- The stop index is not included in a slice.")

	print("\nMini challenge")
	print("-" * 40)
	word = "notebook"
	print(f"word = {word!r}")
	print("Try predicting word[0], word[3], word[2:6], word[-3:], and word[::-1].")

	print("\n=== Done ===")
	return 0


raise SystemExit(main(sys.argv))
