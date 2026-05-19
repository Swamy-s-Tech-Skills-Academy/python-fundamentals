"""Working sample: sort and reverse lists with numbers and strings."""

# Filename: src/Working/module6/06_sample.py

import sys

HELP_TEXT = """06_sample.py

Purpose
	Demonstrate sort() and reverse() with both numeric data and text data.

Usage
	python src/Working/module6/06_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	print("=== Working Sample 06: sort() and reverse() ===\n")

	numbers = [20, 10, 50, 40, 60, 25, 30, 45]
	print(f"Original numbers: {numbers}")

	numbers.sort()
	print(f"After sort(): {numbers}")

	numbers.reverse()
	print(f"After reverse(): {numbers}")

	languages = ["python", "java", "C", "r", "R"]
	print(f"\nOriginal words: {languages}")

	languages.sort()
	print(f"After sort(): {languages}")
	return 0


raise SystemExit(main(sys.argv))