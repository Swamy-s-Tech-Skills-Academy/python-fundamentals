"""Demonstrates complex assignment and type conversion in Python."""

# Filename: src/Working/Module1/04_sample.py

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

    # --- Chained assignment: same value to multiple names ---
    # Standard delivery zones all share a 2-business-day lead time.
    north = south = central = east = 2
    print(
        "Standard zones (days) — "
        f"North: {north}, South: {south}, Central: {central}, East: {east}"
    )

    # Remote delivery zones share a 5-business-day lead time.
    highland = island = offshore = border = 5
    print(
        "Remote zones   (days) — "
        f"Highland: {highland}, Island: {island}, Offshore: {offshore}, Border: {border}"
    )

    # --- Multiple targets, different values in one line (tuple unpacking) ---
    # Pair a city with its nearest fulfilment hub in a single statement.
    city, hub = "Hyderabad", "Pune"
    print(f"\nCity: {city!r},  Nearest hub: {hub!r}")


# ---------------------------------------------------------------------------
# Section 2 — Type Conversion
# ---------------------------------------------------------------------------


def demo_type_conversion() -> None:
    """Show how str(), int(), float(), and bool() convert between types."""

    print("\n=== Type Conversion ===\n")

    # Original variables and their types
    sensor_code = "HUMIDITY_02"  # str
    zone_number = 5  # int
    humidity_percent = 63.4  # float
    is_alert_active = False  # bool

    print("Original values and types:")
    variables = (
        ("sensor_code", sensor_code),
        ("zone_number", zone_number),
        ("humidity_percent", humidity_percent),
        ("is_alert_active", is_alert_active),
    )
    for name, value in variables:
        print(f"  {name} = {value!r:16}  ->  {type(value).__name__}")

    print()

    # int  →  str  (e.g. building a log message)
    zone_as_text = str(zone_number)
    print(
        f"str({zone_number})          -> {zone_as_text!r}  ({type(zone_as_text).__name__})"
    )

    # float  →  int  (truncates decimal — useful for whole-number comparisons)
    humidity_whole = int(humidity_percent)
    print(
        f"int({humidity_percent})       -> {humidity_whole}    ({type(humidity_whole).__name__})"
    )

    # bool  →  float  (False == 0.0, used in weighted calculations)
    alert_weight = float(is_alert_active)
    print(
        f"float({is_alert_active})   -> {alert_weight}   ({type(alert_weight).__name__})"
    )

    # str (numeric)  →  int  (reading a value stored as text)
    raw_port = "8080"
    port_number = int(raw_port)
    print(f'int("{raw_port}")      -> {port_number}    ({type(port_number).__name__})')

    # str (non-numeric)  →  int  — demonstrates ValueError
    print()
    print(f"Attempting int({sensor_code!r}) ...")
    try:
        _ = int(sensor_code)
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
