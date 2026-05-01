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
    the type() function, and variable assignment / deletion.

Usage
    python sample1.py
"""


def demo_data_types() -> None:
    """Show the four primary data types and arithmetic with them."""
    print("--- Numbers ---")
    print(7)           # int
    print(5.9)         # float
    print(7 * 7)       # int arithmetic  → 49
    print(5.2 + 6.8)   # float arithmetic → 12.0

    print("\n--- Strings ---")
    print("hello data science")
    print('hello data science')   # single quotes work too

    print("\n--- Booleans in arithmetic ---")
    print(True * 7)    # True == 1  → 7
    print(False * 7)   # False == 0 → 0


def demo_type_function() -> None:
    """Show how type() reveals the data type of any value."""
    print("--- type() ---")
    print(type(5.9))               # <class 'float'>
    print(type(7))                 # <class 'int'>
    print(type("hello data science"))  # <class 'str'>
    print(type(True))              # <class 'bool'>
    print(type(5.2 + 6.8))        # <class 'float'>


def demo_variables() -> None:
    """Show variable assignment, reassignment, del, and NameError."""
    print("--- Assignment ---")
    a = "november"
    print(a)           # november

    b = 9
    c = 5.8
    d = True
    print(b, c, d)     # 9  5.8  True

    print("\n--- Reassignment ---")
    a = "october"
    print(a)           # october — previous value is gone

    print("\n--- del and NameError ---")
    a = "september"
    print(a)           # september
    del a
    # Accessing a now would raise:
    #   NameError: name 'a' is not defined
    # Tip: comment out `del a` above if you need to reuse the variable later.

    print("\n--- type() on variables ---")
    b = 9
    c = 5.8
    d = True
    print(type(b))     # <class 'int'>
    print(type(c))     # <class 'float'>
    print(type(d))     # <class 'bool'>


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
