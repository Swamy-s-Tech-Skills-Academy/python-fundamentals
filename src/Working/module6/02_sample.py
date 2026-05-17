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

	premier_league = ["Manchester", "Chelsea", "Arsenal", "Liverpool", "Everton"]
	mixed_list = [20, 7.8, True, "football", premier_league]

	print("=== Working Module 6: Indexing and Slicing ===\n")
	print(f"mixed_list = {mixed_list}")
	print(f"mixed_list[0] = {mixed_list[0]}")
	print(f"mixed_list[1] = {mixed_list[1]}")
	print(f"mixed_list[2] = {mixed_list[2]}")
	print(f"mixed_list[3] = {mixed_list[3]}")
	print(f"mixed_list[4] = {mixed_list[4]}")
	print(f"mixed_list[4][0] = {mixed_list[4][0]}")
	print(f"mixed_list[0:3] = {mixed_list[0:3]}")
	print(f"mixed_list[3:] = {mixed_list[3:]}")

	try:
		print(mixed_list[8])
	except IndexError as error:
		print(f"Accessing index 8 raises: {error}")
	return 0


raise SystemExit(main(sys.argv))