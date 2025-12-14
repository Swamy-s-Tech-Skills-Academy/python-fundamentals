# Filename: src/L1/S2/03_type_conversion.py

# Session 2: Variables & Data Types
# Practice: Converting between data types

print("=== Type Conversion Examples ===\n")

# Converting to Integer
print("1. CONVERTING TO INTEGER (int()):")
age_str = "25"
age_int = int(age_str)
print(f"   '{age_str}' (str) → {age_int} (int)")

price_float = 19.99
price_int = int(price_float)
print(f"   {price_float} (float) → {price_int} (int)")

# Converting to Float
print("\n2. CONVERTING TO FLOAT (float()):")
price_str = "19.99"
price_float = float(price_str)
print(f"   '{price_str}' (str) → {price_float} (float)")

age_int = 25
age_float = float(age_int)
print(f"   {age_int} (int) → {age_float} (float)")

# Converting to String
print("\n3. CONVERTING TO STRING (str()):")
age = 25
age_str = str(age)
print(f"   {age} (int) → '{age_str}' (str)")

price = 19.99
price_str = str(price)
print(f"   {price} (float) → '{price_str}' (str)")

# Converting to Boolean
print("\n4. CONVERTING TO BOOLEAN (bool()):")
print(f"   bool(1): {bool(1)}")
print(f"   bool(0): {bool(0)}")
print(f"   bool('hello'): {bool('hello')}")
print(f"   bool(''): {bool('')}")

# Practical Example: User Input
print("\n=== Practical Example: User Input ===")
print("(This would normally come from input(), showing conversion)")
age_input = "25"  # Simulating input("Enter your age: ")
age = int(age_input)
print(f"   User entered: '{age_input}' (string)")
print(f"   Converted to: {age} (integer)")
print(f"   Can now do math: {age} + 5 = {age + 5}")

# Combining strings and numbers
print("\n=== Combining Strings and Numbers ===")
name = "Alice"
age = 25
# Method 1: Using str() conversion
message1 = "I am " + str(age) + " years old"
print(f"   Method 1: {message1}")

# Method 2: Using f-strings (easier!)
message2 = f"I am {age} years old"
print(f"   Method 2: {message2}")

