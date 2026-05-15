"""Working draft: extended string slicing with negative indexes and steps."""

# Filename: src/Working/module5/08_sample.py

import sys

HELP_TEXT = """08_sample.py

Purpose
	Demonstrate negative indexing, negative slicing, and step-based slicing
	with simple string examples.

Usage
	python src/Working/module5/08_sample.py
"""


def show_result(label: str, value: object) -> None:
	print(f"{label:<32} -> {value!r}")


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	car = "ferrari"
	print(f"car = {car!r}\n")

	print("Negative indexing")
	print("-" * 40)
	show_result("Last character", car[-1])
	show_result("Second-to-last character", car[-2])
	show_result("Fifth character from end", car[-5])

	print("\nNegative slicing")
	print("-" * 40)
	show_result("car[-5:-2]", car[-5:-2])
	show_result("car[-4:]", car[-4:])
	show_result("car[:-3]", car[:-3])

	print("\nStep slicing")
	print("-" * 40)
	show_result("car[0:7:2]", car[0:7:2])
	show_result("car[0:7:3]", car[0:7:3])
	show_result("car[::2]", car[::2])
	show_result("car[::-1]", car[::-1])
	show_result("car[2::4]", car[2::4])

	print("\nKey ideas")
	print("-" * 40)
	print("- Negative indexes start from -1 at the last character.")
	print("- Slice start is included, slice stop is excluded.")
	print("- A step of 2 skips every other character.")
	print("- A step of -1 reverses the string.")

	print("\nMini challenge")
	print("-" * 40)
	word = "notebook"
	print(f"word = {word!r}")
	print("Predict these results before running them in the REPL:")
	print("word[-1], word[-4:-1], word[::3], and word[::-2]")

	print("\n=== Done ===")
	return 0


raise SystemExit(main(sys.argv))