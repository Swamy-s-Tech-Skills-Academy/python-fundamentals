"""Working sample: add and remove list items by index."""

# Filename: src/Working/module6/05_sample.py

import sys

HELP_TEXT = """05_sample.py

Purpose
	Demonstrate insert() and pop() when you want to target a specific
	list position.

Usage
	python src/Working/module6/05_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	print("=== Working Sample 05: insert() and pop() ===\n")

	numbers = [10, 20, 30, 40, 50, 60]
	print(f"Start: {numbers}")

	numbers.insert(2, 195)
	print(f"After insert(2, 195): {numbers}")

	removed_value = numbers.pop(2)
	print(f"pop(2) returned: {removed_value}")
	print(f"After pop(2): {numbers}")
	return 0


raise SystemExit(main(sys.argv))