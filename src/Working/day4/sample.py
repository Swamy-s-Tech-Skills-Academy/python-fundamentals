# Type Conversion — Working / day4 sample
# Concepts: str(), int(), float(), bool() | what can and cannot convert

# ---------------------------------------------------------------------------
# Starting variables — one of each core type
# ---------------------------------------------------------------------------
a = "september"   # str
b = 9             # int
c = 5.8           # float
d = True          # bool

print("=== Original types ===")
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# ---------------------------------------------------------------------------
# Convert to different types
# ---------------------------------------------------------------------------
print("\n=== Conversions ===")

converted_b = str(b)          # int  → str
converted_c = int(c)          # float → int  (truncates, does NOT round)
converted_d = float(d)        # bool → float (True → 1.0)

print(f"str({b})      -> {converted_b!r}  type={type(converted_b).__name__}")
print(f"int({c})    -> {converted_c}     type={type(converted_c).__name__}  (truncated, not rounded)")
print(f"float({d})  -> {converted_d}   type={type(converted_d).__name__}  (True is 1 in Python)")

# ---------------------------------------------------------------------------
# int() on a non-numeric string → ValueError
# ---------------------------------------------------------------------------
print("\n=== int() on a word string — expected ValueError ===")
try:
    converted_a = int(a)      # "september" has no numeric value
except ValueError as err:
    print(f"ValueError: {err}")
print("Takeaway: int() only works when the string contains digits.")

# ---------------------------------------------------------------------------
# int() on a numeric string — this DOES work
# ---------------------------------------------------------------------------
print("\n=== int() on a numeric string — works fine ===")
e = "8"
converted_e = int(e)
print(f"int({e!r}) -> {converted_e}  type={type(converted_e).__name__}")
