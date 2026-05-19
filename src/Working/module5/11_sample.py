"""Working draft: string formatting with the .format() method."""

# Filename: src/Working/module5/11_sample.py

import sys

HELP_TEXT = """11_sample.py

Purpose
	Demonstrate how the .format() method fills placeholders in order,
	with direct values, and by using indexed placeholders.

Usage
	python src/Working/module5/11_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	shopping_template = "I bought {} kilos of {} from the market."
	kilos = 2
	vegetable = "tomatoes"

	print(f"shopping_template = {shopping_template!r}\n")
	print(shopping_template.format(kilos, vegetable))
	print(shopping_template.format(3.5, "potatoes"))

	fixture_template = "{} vs {} finished {} - {}."
	teams_and_score = fixture_template.format("Lions", "Tigers", 4, 3)
	reordered_result = "{3} vs {2} finished {1} - {0}.".format(3, 4, "Tigers", "Lions")

	print("\nMatch examples")
	print("-" * 40)
	print(teams_and_score)
	print(reordered_result)

	print("\nKey ideas")
	print("-" * 40)
	print("- Empty braces {} are filled from left to right.")
	print("- .format() can receive variables or direct values.")
	print("- Numbered placeholders such as {0} or {3} let you reorder items.")
	print("- The numbers inside numbered placeholders refer to argument positions.")

	print("\nMini challenge")
	print("-" * 40)
	print("Create a sentence with three placeholders and print it once in normal order and once in a different order.")

	print("\n=== Done ===")
	return 0


raise SystemExit(main(sys.argv))