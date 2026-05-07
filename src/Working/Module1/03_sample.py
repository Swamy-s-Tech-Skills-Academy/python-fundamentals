"""Day 2: PEP 8 — Writing Readable Python Code.

What you practice here:
- Choosing meaningful, descriptive variable names
- Using snake_case (underscores, no spaces)
- Applying 4-space indentation correctly
- Spacing rules around brackets and operators
- Writing clear, well-formed comments

Why PEP 8 matters:
    PEP 8 (Python Enhancement Proposal 8) is the official style guide
    for Python, authored by Guido van Rossum in 2001. It exists so
    that code written by many different people still reads as if one
    person wrote it — making collaboration and maintenance far easier.
"""

# Filename: src/Working/Module1/03_sample.py

import sys

HELP_TEXT = """pep8_style.py

Purpose
    Demonstrate PEP 8 naming, indentation, spacing, and comment rules
    using a weather-station data scenario as the working context.

Usage
    python pep8_style.py
"""


# ---------------------------------------------------------------------------
# 1. Naming Conventions
# ---------------------------------------------------------------------------
# Rule: names should be specific enough that a reader knows exactly
#       what the variable holds — avoid single letters or vague words.
# Rule: use underscores to separate words in a name (snake_case).
#
#   BAD  → t, temp, data, val
#   GOOD → temperature_celsius, wind_speed_kmh, station_is_online


def demo_naming() -> None:
    """Show the difference between vague and descriptive names."""

    print("=== 1. Naming Conventions ===\n")

    # --- Vague names (hard to understand at a glance) ---
    raw_a = 22.4  # What is this measuring? Units?
    raw_b = 14.0  # Wind? Weight? Width?
    raw_c = True  # Status of what?

    # --- Descriptive names (self-explanatory) ---
    temperature_celsius = 22.4
    wind_speed_kmh = 14.0
    station_is_online = True

    print(f"Temperature : {temperature_celsius} C")
    print(f"Wind speed  : {wind_speed_kmh} km/h")
    print(f"Station up  : {station_is_online}")

    # Suppressing the "unused variable" warning for the vague examples
    _ = (raw_a, raw_b, raw_c)


# ---------------------------------------------------------------------------
# 2. Indentation — 4 spaces per level
# ---------------------------------------------------------------------------
# Rule: each inner block is indented by exactly 4 spaces.
# Rule: when a function call has too many arguments to fit on one line,
#       wrap them — starting the continuation on the NEXT line with an
#       extra indent level (not on the same line as the opening bracket).


def record_reading(station_id, temperature_celsius, humidity_percent, wind_speed_kmh):
    """Return a formatted string summarising one weather reading."""
    # Each line of the function body is indented 4 spaces from `def`
    summary = (
        f"Station {station_id}: "
        f"{temperature_celsius}C | "
        f"{humidity_percent}% RH | "
        f"{wind_speed_kmh} km/h"
    )
    return summary


def demo_indentation() -> None:
    """Show correct multi-line argument wrapping."""

    print("=== 2. Indentation ===\n")

    reading = record_reading(
        station_id="WS-04",
        temperature_celsius=22.4,
        humidity_percent=61,
        wind_speed_kmh=14.0,
    )
    print(reading)


# ---------------------------------------------------------------------------
# 3. Spaces Inside Brackets and Around Punctuation
# ---------------------------------------------------------------------------
# Rule: NO space immediately after ( or [ or {
# Rule: NO space immediately before ) or ] or }
# Rule: NO space before a comma or colon; ONE space after them
#
#   BAD  → readings[ 0 ]   or   readings [0]
#   GOOD → readings[0]
#
#   BAD  → record_reading( "WS-04" , 22.4 )
#   GOOD → record_reading("WS-04", 22.4)


def demo_bracket_spacing() -> None:
    """Illustrate correct spacing inside brackets and around commas."""

    print("=== 3. Bracket & Comma Spacing ===\n")

    readings = [18.0, 20.5, 22.4, 21.1, 19.8]

    # Correct: no padding inside brackets
    first = readings[0]
    last = readings[-1]

    print(f"First reading : {first}")
    print(f"Last reading  : {last}")
    print(f"All readings  : {readings}")


# ---------------------------------------------------------------------------
# 4. Spaces Around Operators
# ---------------------------------------------------------------------------
# Rule: put ONE space on each side of binary operators
#       (+  -  *  /  //  %  **  =  ==  !=  <  >  <=  >=)
#
#   BAD  → avg=total/count   or   avg=total /count
#   GOOD → avg = total / count


def demo_operator_spacing() -> None:
    """Show correct spacing around arithmetic and comparison operators."""

    print("=== 4. Operator Spacing ===\n")

    readings = [18.0, 20.5, 22.4, 21.1, 19.8]

    total = sum(readings)
    count = len(readings)
    average = total / count
    variance = sum((reading_value - average) ** 2 for reading_value in readings) / count

    print(f"Total    : {total:.1f}")
    print(f"Count    : {count}")
    print(f"Average  : {average:.2f} C")
    print(f"Variance : {variance:.3f}")

    above_average = average + 1.5
    print(f"\nReadings above {above_average:.2f} C:")
    for reading in readings:
        if reading > above_average:
            print(f"  {reading}")


# ---------------------------------------------------------------------------
# 5. Comment Style
# ---------------------------------------------------------------------------
# Rule: use # followed by a single space before your comment text
# Rule: inline comments sit at least 2 spaces after the code they explain
# Rule: keep comment lines to ~72 characters for readability
# Rule: for multi-line comments, put a # at the start of every line
# Rule: leave two blank lines between a block comment and the code below


# This section computes daily summary statistics from a list of hourly
# temperature readings. It finds the min, max, and mean, then flags
# any reading that deviates from the mean by more than one degree.


def demo_comments() -> None:
    """Show comment placement and formatting conventions."""

    print("=== 5. Comment Style ===\n")

    hourly_temps = [17.2, 18.0, 19.5, 21.3, 22.4, 21.8, 20.1, 18.6]

    min_temp = min(hourly_temps)  # lowest reading of the day
    max_temp = max(hourly_temps)  # highest reading of the day
    mean_temp = sum(hourly_temps) / len(hourly_temps)

    print(f"Min  : {min_temp} C")
    print(f"Max  : {max_temp} C")
    print(f"Mean : {mean_temp:.2f} C")

    # Flag readings that differ from the mean by more than 1 degree
    threshold = 1.0
    anomalies = [
        temp_value
        for temp_value in hourly_temps
        if abs(temp_value - mean_temp) > threshold
    ]

    if anomalies:
        print(f"\nAnomalous readings (>{threshold} deg from mean): {anomalies}")
    else:
        print("\nAll readings are within the expected range.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    demo_naming()
    print()
    demo_indentation()
    print()
    demo_bracket_spacing()
    print()
    demo_operator_spacing()
    print()
    demo_comments()
    return 0


raise SystemExit(main(sys.argv))
