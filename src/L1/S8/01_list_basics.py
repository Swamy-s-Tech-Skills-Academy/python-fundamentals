"""Session 8: list creation, indexing, slicing, and item replacement."""

# Filename: src/L1/S8/01_list_basics.py

import sys

HELP_TEXT = """01_list_basics.py

Purpose
    Demonstrate how to create lists, inspect them, access items by index, slice
    ranges, and replace one item.

Usage
    python src/L1/S8/01_list_basics.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== List Basics Demo ===\n")

    # Creating lists
    print("--- Creating Lists ---")
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed = [42, "hello", 3.14, True]
    empty = []

    print(f"Numbers: {numbers}")
    print(f"Fruits: {fruits}")
    print(f"Mixed: {mixed}")
    print(f"Empty: {empty}")

    # List properties
    print("\n--- List Properties ---")
    print(f"Length of fruits: {len(fruits)}")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'mango' in fruits: {'mango' in fruits}")

    # Indexing
    print("\n--- Indexing ---")
    print(f"fruits[0] = {fruits[0]}")
    print(f"fruits[1] = {fruits[1]}")
    print(f"fruits[-1] = {fruits[-1]}")

    # Slicing
    print("\n--- Slicing ---")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"numbers = {numbers}")
    print(f"numbers[2:5] = {numbers[2:5]}")
    print(f"numbers[:4] = {numbers[:4]}")
    print(f"numbers[6:] = {numbers[6:]}")
    print(f"numbers[::2] = {numbers[::2]}")
    print(f"numbers[::-1] = {numbers[::-1]}")

    # Modifying
    print("\n--- Modifying ---")
    colors = ["red", "green", "blue"]
    print(f"Original: {colors}")
    colors[1] = "yellow"
    print(f"After colors[1] = 'yellow': {colors}")
    return 0


raise SystemExit(main(sys.argv))
