"""Demonstrates complex assignment and type conversion in Python."""

import sys

HELP_TEXT = """sample.py

Purpose
    Shows two related concepts:
      1. Complex / chained variable assignment
      2. Type conversion between str, int, float, and bool

Usage
    python sample.py
"""


# ---------------------------------------------------------------------------
# Section 1 — Complex Assignment
# ---------------------------------------------------------------------------

def demo_complex_assignment() -> None:
    """Illustrate chained and multiple-target assignment."""

    print("=== Complex Assignment ===\n")

    # Multiple variables, same value (chained assignment)
    january = march = may = july = august = october = december = 31
    print(f"Months with 31 days - August: {august}, December: {december}")

    # Separate assignments for 30-day months (verbose style)
    april = june = september = november = 30
    print(f"Months with 30 days - April: {april}, June: {june}")

    # Multiple targets, different values in one line (tuple unpacking)
    python, java = "data", "science"
    print(f"\npython = {python!r},  java = {java!r}")


# ---------------------------------------------------------------------------
# Section 2 — Type Conversion
# ---------------------------------------------------------------------------

def demo_type_conversion() -> None:
    """Show how str(), int(), float(), and bool() convert between types."""

    print("\n=== Type Conversion ===\n")

    # Original variables and their types
    a = "september"
    b = 9
    c = 5.8
    d = True

    print("Original values and types:")
    for name, value in (("a", a), ("b", b), ("c", c), ("d", d)):
        print(f"  {name} = {value!r:12}  ->  {type(value).__name__}")

    print()

    # int  →  str
    converted_b = str(b)
    print(f"str({b})         -> {converted_b!r}  ({type(converted_b).__name__})")

    # float  →  int  (truncates decimal)
    converted_c = int(c)
    print(f"int({c})       -> {converted_c}    ({type(converted_c).__name__})")

    # bool  →  float  (True == 1, False == 0)
    converted_d = float(d)
    print(f"float({d})   -> {converted_d}   ({type(converted_d).__name__})")

    # str (numeric)  →  int
    e = "8"
    converted_e = int(e)
    print(f'int("{e}")        -> {converted_e}    ({type(converted_e).__name__})')

    # str (non-numeric)  →  int  — shows ValueError
    print()
    print("Attempting int('september') ...")
    try:
        _ = int(a)
    except ValueError as err:
        print(f"  ValueError: {err}")
        print("  (Only numeric strings can be converted to int/float.)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_complex_assignment()
    demo_type_conversion()
    return 0


raise SystemExit(main(sys.argv))
