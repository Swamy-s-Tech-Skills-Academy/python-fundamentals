"""Working Module 6 sample: indexing and slicing list data."""

# Filename: src/Working/module6/02_sample.py

import sys

HELP_TEXT = """02_sample.py

Purpose
	Demonstrate list indexing, nested indexing, slicing, and how Python reacts
	to an out-of-range index.

Usage
	python src/Working/module6/02_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	reading_list = ["lesson notes", "worked example", "quiz", "review"]
	mixed_list = ["Session 8", 35, False, reading_list]

	print("=== Working Module 6: Indexing and Slicing ===\n")
	print(f"mixed_list = {mixed_list}")
	print(f"mixed_list[0] = {mixed_list[0]}")
	print(f"mixed_list[1] = {mixed_list[1]}")
	print(f"mixed_list[2] = {mixed_list[2]}")
	print(f"mixed_list[3] = {mixed_list[3]}")
	print(f"mixed_list[3][1] = {mixed_list[3][1]}")
	print(f"mixed_list[0:3] = {mixed_list[0:3]}")
	print(f"mixed_list[2:] = {mixed_list[2:]}")

	try:
		print(mixed_list[6])
	except IndexError as error:
		print(f"Accessing index 6 raises: {error}")
	return 0


raise SystemExit(main(sys.argv))