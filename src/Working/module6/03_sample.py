"""Working Module 6 sample: updating and deleting list items."""

# Filename: src/Working/module6/03_sample.py

import sys

HELP_TEXT = """03_sample.py

Purpose
	Demonstrate how to add items, replace one item, replace a slice, and
	delete an item from a list.

Usage
	python src/Working/module6/03_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	countries = ["USA", "Germany", "Turkey", "Egypt"]

	print("=== Working Module 6: Updating Lists ===\n")
	print(f"Start: {countries}")

	countries = countries + ["Greece"]
	print(f"After adding one item with +: {countries}")

	countries[0] = "France"
	print(f"After countries[0] = 'France': {countries}")

	countries[0:3] = ["Japan", "Syria", "Italy"]
	print(f"After replacing the first three items: {countries}")

	del countries[-1]
	print(f"After del countries[-1]: {countries}")
	return 0


raise SystemExit(main(sys.argv))