"""Day 5: Type conversion drill.

Builds on Day 4: same conversion tools (str, int, float, bool), in a shorter
story so you can read the patterns without delivery-zone context.
"""

# Filename: src/Working/Module1/05_sample.py

import sys

HELP_TEXT = """05_sample.py

Purpose
    Practice str(), int(), float(), and bool() conversions.

Usage
    python 05_sample.py

Topics Covered
    - Reading type() alongside the value you stored
    - Typical safe conversions beginners use first
    - ValueError when int() cannot parse the string as an integer

Next script
    06_sample.py - combine numbers with arithmetic operators.
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print(
        "Day 5: Same casts as Day 4 - repeat until int('8') feels obvious.\n"
    )

    print("=== Original values and types ===")
    month_name = "september"  # str
    month_number = 9  # int
    discount_rate = 5.8  # float
    is_active = True  # bool

    print(type(month_name), month_name)
    print(type(month_number), month_number)
    print(type(discount_rate), discount_rate)
    print(type(is_active), is_active)

    print("\n=== Valid conversions ===")
    converted_month_number = str(month_number)  # int -> str
    converted_discount_rate = int(discount_rate)  # float -> int (truncates)
    converted_is_active = float(is_active)  # bool -> float (True -> 1.0)

    print(
        f"str({month_number}) -> {converted_month_number!r} "
        f"(type={type(converted_month_number).__name__})"
    )
    print(
        f"int({discount_rate}) -> {converted_discount_rate} "
        f"(type={type(converted_discount_rate).__name__}, truncated)"
    )
    print(
        f"float({is_active}) -> {converted_is_active} "
        f"(type={type(converted_is_active).__name__})"
    )

    print("\n=== Invalid conversion example ===")
    try:
        _ = int(month_name)  # "september" is not numeric text
    except ValueError as err:
        print(f"ValueError: {err}")
    print(
        "Takeaway: int(some_text) works when Python can parse the entire string "
        "as an integer (for example '8'), not as a word like 'september'."
    )

    print("\n=== Numeric string conversion ===")
    score_text = "8"
    score_number = int(score_text)
    print(f"int({score_text!r}) -> {score_number} (type={type(score_number).__name__})")

    return 0


raise SystemExit(main(sys.argv))
