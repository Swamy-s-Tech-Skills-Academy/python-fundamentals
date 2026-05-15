"""Working draft: combining and repeating strings with operators."""

# Filename: src/Working/module5/09_sample.py

import sys

HELP_TEXT = """09_sample.py

Purpose
	Demonstrate how +, +=, and *= can be used with strings, along with
	print(*text) for spaced character output.

Usage
	python src/Working/module5/09_sample.py
"""


def main(argv: list[str]) -> int:
	if any(arg in {"-h", "--help"} for arg in argv[1:]):
		print(HELP_TEXT)
		return 0

	teams = "Lakers"
	print(f"teams starts as {teams!r}")

	combined = teams + " Celtics"
	print(f"teams + ' Celtics'          -> {combined!r}")

	teams = combined
	teams += " Dallas"
	print(f"After += ' Dallas'          -> {teams!r}")

	repeated = teams * 3
	print(f"teams * 3                   -> {repeated!r}")

	chant = "Go! "
	chant *= 4
	print(f"\nchant after *= 4           -> {chant!r}")

	city = "barcelona"
	print(f"\ncity = {city!r}")
	print("print(*city) output:")
	print(*city)

	print("\nKey ideas")
	print("-" * 40)
	print("- + joins strings into one larger string.")
	print("- += updates the same variable with extra text.")
	print("- * repeats a string a chosen number of times.")
	print("- print(*text) prints each character as a separate argument.")

	print("\nMini challenge")
	print("-" * 40)
	print("Try building a banner with '=' * 20 and a team name in the middle.")

	print("\n=== Done ===")
	return 0


raise SystemExit(main(sys.argv))