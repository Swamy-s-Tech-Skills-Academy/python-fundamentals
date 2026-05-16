"""String formatting with the .format() method."""

# Filename: src/L1/S8/11_string_format_method.py

import sys

HELP_TEXT = """11_string_format_method.py

Purpose
    Demonstrate how the .format() method fills placeholders in order,
    with direct values, and by using indexed placeholders.

Usage
    python src/L1/S8/11_string_format_method.py
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
    normal_order = fixture_template.format("Lions", "Tigers", 4, 3)
    indexed_order = "{3} vs {2} finished {1} - {0}.".format(3, 4, "Tigers", "Lions")

    print("\n=== Match examples ===")
    print(normal_order)
    print(indexed_order)

    print("\nRemember:")
    print("- Empty braces {} are filled from left to right.")
    print("- .format() can receive variables or direct values.")
    print("- Numbered placeholders such as {0} and {3} let you reorder values.")
    print("- The numbers refer to argument positions inside .format().")

    return 0


raise SystemExit(main(sys.argv))