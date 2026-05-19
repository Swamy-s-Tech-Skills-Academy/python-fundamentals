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

	study_topics = ["variables", "conditions", "loops", "functions"]
	print("Study topics list:")
	print(study_topics)
	print(f"Type: {type(study_topics).__name__}")

	lesson_snapshot = [3, "Wednesday", True, study_topics]
	print("\nMixed list with a nested topic list:")
	print(lesson_snapshot)
	print(f"Length: {len(lesson_snapshot)}")

	reminder_tuple = ("practice", 25, False, study_topics)
	converted_list = list(reminder_tuple)
	print("\nTuple converted into a list:")
	print(converted_list)
	print(f"Converted type: {type(converted_list).__name__}")
	return 0


raise SystemExit(main(sys.argv))