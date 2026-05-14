"""Working draft: string indexing and slicing.

Run: python src/Working/module5/07_sample.py
"""

from __future__ import annotations


def show_slice(label: str, text: str, start: int | None, stop: int | None) -> None:
	print(f"{label:<24} -> {text[start:stop]!r}")


def main() -> None:
	course_name = "python"
	print(f"course_name = {course_name!r}\n")

	print("Indexing examples")
	print("-" * 40)
	print(f"First character        -> {course_name[0]!r}")
	print(f"Third character        -> {course_name[2]!r}")
	print(f"Last character         -> {course_name[-1]!r}")

	print("\nSlicing examples")
	print("-" * 40)
	show_slice("Characters 1 to 4", course_name, 1, 5)
	show_slice("From index 2 onward", course_name, 2, None)
	show_slice("From start to index 4", course_name, None, 4)
	show_slice("Middle section", course_name, 1, 4)

	print("\nRemember:")
	print("- Indexes start at 0 in Python.")
	print("- The start index is included in a slice.")
	print("- The stop index is not included in a slice.")

	print("\nMini challenge")
	print("-" * 40)
	word = "notebook"
	print(f"word = {word!r}")
	print(f"Try predicting word[0], word[3], word[2:6], and word[-3:] before changing this file.")

	print("\n=== Done ===")


if __name__ == "__main__":
	main()
'ferra'
