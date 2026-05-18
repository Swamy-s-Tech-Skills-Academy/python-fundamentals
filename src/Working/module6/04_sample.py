"""Working sample: inspect list methods, then append and remove values."""

# Filename: src/Working/module6/04_sample.py

import sys

HELP_TEXT = """04_sample.py

Purpose
	Show how to inspect list methods with dir(), then practice append()
	and remove() on a simple number list.

Usage
	python src/Working/module6/04_sample.py
"""


def show_public_list_methods() -> None:
	public_methods = []

	for method_name in dir(list):
		if not method_name.startswith("_"):
			public_methods.append(method_name)

	print("Public list methods:")
	print(public_methods)


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	print("=== Working Sample 04: append() and remove() ===\n")
	show_public_list_methods()

	numbers = [10, 20, 30, 40, 50, 60]
	print(f"\nStart: {numbers}")

	numbers.append(70)
	print(f"After append(70): {numbers}")

	numbers.remove(70)
	print(f"After remove(70): {numbers}")
	return 0


raise SystemExit(main(sys.argv))