"""Working draft: modern string formatting with f-strings."""

# Filename: src/Working/module5/12_sample.py

import sys

HELP_TEXT = """12_sample.py

Purpose
	Demonstrate how f-strings place variables, expressions, and method
	results directly inside a string.

Usage
	python src/Working/module5/12_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	kilos = 2
	vegetable = "tomatoes"
	market_message = f"I bought {kilos} kilos of {vegetable} from the market."

	print(f"kilos = {kilos}")
	print(f"vegetable = {vegetable!r}\n")
	print(market_message)

	age_message = f"I am {2 ** 5} years old in this pretend example."
	print("\nExpression inside braces")
	print("-" * 40)
	print(age_message)

	name = "joseph"
	shout_name = f"My name is {name.upper()}."

	print("\nMethod call inside braces")
	print("-" * 40)
	print(shout_name)

	print("\nKey ideas")
	print("-" * 40)
	print("- Add f before the opening quote to create an f-string.")
	print("- Put variables directly inside braces to insert their values.")
	print("- Expressions like 2 ** 5 are evaluated before printing.")
	print("- Method calls such as name.upper() can be used inside braces.")

	print("\nMini challenge")
	print("-" * 40)
	print("Store a city name in a variable and print it in title case with an f-string.")

	print("\n=== Done ===")
	return 0


raise SystemExit(main(sys.argv))