"""Working Module 6 sample: adding, changing, and deleting list items."""

# Filename: src/Working/module6/03_sample.py

import sys

HELP_TEXT = """03_sample.py

Purpose
	Demonstrate how to add an item with list concatenation, replace one
	item, replace a slice, and delete an item from a list.

Usage
	python src/Working/module6/03_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	country_list = ["USA", "Germany", "Turkey", "Egypt"]

	print("=== Working Module 6: Updating Lists ===\n")
	print(f"Start: {country_list}")

	country_list = country_list + ["Greece"]
	print(f"After country_list + ['Greece']: {country_list}")

	country_list[0] = "France"
	print(f"After country_list[0] = 'France': {country_list}")

	country_list[0:3] = ["Japan", "Syria", "Italy"]
	print(f"After country_list[0:3] = ['Japan', 'Syria', 'Italy']: {country_list}")

	del country_list[-1]
	print(f"After del country_list[-1]: {country_list}")
	return 0


raise SystemExit(main(sys.argv))