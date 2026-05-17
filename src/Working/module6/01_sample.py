"""Working Module 6 sample: creating beginner-friendly lists."""

# Filename: src/Working/module6/01_sample.py

import sys

HELP_TEXT = """01_sample.py

Purpose
	Demonstrate list creation, mixed-type lists, nested lists, and converting a
	tuple into a list.

Usage
	python src/Working/module6/01_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	print("=== Working Module 6: Creating Lists ===\n")

	premier_league = ["Manchester", "Chelsea", "Arsenal", "Liverpool", "Everton"]
	print("Premier League teams:")
	print(premier_league)
	print(f"Type: {type(premier_league).__name__}")

	mixed_list = [20, 7.8, True, "football", premier_league]
	print("\nMixed list with a nested list:")
	print(mixed_list)
	print(f"Length: {len(mixed_list)}")

	values = (20, 7.8, "football", premier_league)
	converted_list = list(values)
	print("\nTuple converted into a list:")
	print(converted_list)
	print(f"Converted type: {type(converted_list).__name__}")
	return 0


raise SystemExit(main(sys.argv))