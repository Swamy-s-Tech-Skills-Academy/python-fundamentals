"""Day 2: Basic Data Types and Variables.

What you practice here:
- Python's four primary data types: int, float, str, bool
- Using the type() function to inspect any value
- Assigning values to variables and reassigning them
- Deleting a variable with del and understanding NameError
"""

# Filename: src/Working/day2/sample1.py

import sys

HELP_TEXT = """sample1.py

Purpose
    Demonstrate basic data types (int, float, str, bool),
    the type() function, and variable assignment / deletion
    using a coffee shop inventory as the working context.

Usage
    python sample1.py
"""


def demo_data_types() -> None:
    """Show the four primary data types and arithmetic with them."""

    print("--- Numbers ---")
    print(48)  # int  — number of cups in stock
    print(3.75)  # float — price per cup
    print(48 * 3.75)  # int * float → float  (total stock value)
    print(1.50 + 0.80)  # float arithmetic   (espresso + milk surcharge)

    print("\n--- Strings ---")
    print("espresso")
    print("flat white")  # single quotes work the same as double quotes

    print("\n--- Booleans in arithmetic ---")
    print(True * 48)  # True == 1  →  48 (full stock)
    print(False * 48)  # False == 0 →   0 (nothing available)


def demo_type_function() -> None:
    """Show how type() reveals the data type of any value."""

    print("--- type() ---")
    print(type(3.75))  # <class 'float'>
    print(type(48))  # <class 'int'>
    print(type("espresso"))  # <class 'str'>
    print(type(True))  # <class 'bool'>
    print(type(1.50 + 0.80))  # <class 'float'>


def demo_variables() -> None:
    """Show variable assignment, reassignment, del, and NameError."""

    print("--- Assignment ---")
    menu_item = "latte"
    print(menu_item)  # latte

    units_in_stock = 48
    unit_price_gbp = 3.75
    item_is_available = True
    print(units_in_stock, unit_price_gbp, item_is_available)  # 48  3.75  True

    print("\n--- Arithmetic with variables ---")
    # Variables hold the actual values, so maths works just like literals
    addon_price = 0.50
    checkout_total = unit_price_gbp + addon_price
    print(checkout_total)  # 4.25

    print("\n--- Reassignment ---")
    menu_item = "flat white"
    print(menu_item)  # flat white — previous value is gone

    print("\n--- del and NameError ---")
    menu_item = "cappuccino"
    print(menu_item)  # cappuccino
    del menu_item
    # Accessing menu_item now raises:
    #   NameError: name 'menu_item' is not defined
    # Tip: comment out del menu_item above if you need to reuse it later.

    print("\n--- type() on variables ---")
    units_in_stock = 48
    unit_price_gbp = 3.75
    item_is_available = True
    print(type(units_in_stock))  # <class 'int'>
    print(type(unit_price_gbp))  # <class 'float'>
    print(type(item_is_available))  # <class 'bool'>


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_data_types()
    print()
    demo_type_function()
    print()
    demo_variables()
    return 0


raise SystemExit(main(sys.argv))
