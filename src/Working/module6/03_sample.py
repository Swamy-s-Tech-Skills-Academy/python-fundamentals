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

	weekend_plan = ["wash bottle", "pack notebook", "charge laptop", "review agenda"]

	print("=== Working Module 6: Updating Lists ===\n")
	print(f"Start: {weekend_plan}")

	weekend_plan.append("set alarm")
	print(f"After append('set alarm'): {weekend_plan}")

	weekend_plan[0] = "fill water bottle"
	print(f"After weekend_plan[0] = 'fill water bottle': {weekend_plan}")

	weekend_plan[1:3] = ["print checklist", "pack charger"]
	print(f"After replacing a slice: {weekend_plan}")

	del weekend_plan[-1]
	print(f"After del weekend_plan[-1]: {weekend_plan}")
	return 0


raise SystemExit(main(sys.argv))