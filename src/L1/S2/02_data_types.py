# Filename: src/L1/S2/02_data_types.py

# Session 2: Variables & Data Types
# Practice: Working with all four data types

print("=== Python's Four Fundamental Data Types ===\n")

# 1. Integers (int)
print("1. INTEGERS (int):")
age = 25
temperature = -10
count = 0
print(f"   age = {age} ({type(age)})")
print(f"   temperature = {temperature} ({type(temperature)})")
print(f"   count = {count} ({type(count)})")

# 2. Floating-Point Numbers (float)
print("\n2. FLOATING-POINT NUMBERS (float):")
height = 5.9
price = 19.99
pi = 3.14159
print(f"   height = {height} ({type(height)})")
print(f"   price = {price} ({type(price)})")
print(f"   pi = {pi} ({type(pi)})")

# 3. Strings (str)
print("\n3. STRINGS (str):")
name = "Alice"
message = 'Hello, World!'
favorite_color = "blue"
print(f"   name = {name} ({type(name)})")
print(f"   message = {message} ({type(message)})")
print(f"   favorite_color = {favorite_color} ({type(favorite_color)})")

# 4. Booleans (bool)
print("\n4. BOOLEANS (bool):")
is_student = True
is_graduated = False
has_license = True
print(f"   is_student = {is_student} ({type(is_student)})")
print(f"   is_graduated = {is_graduated} ({type(is_graduated)})")
print(f"   has_license = {has_license} ({type(has_license)})")

# Using isinstance() to check types
print("\n=== Type Checking with isinstance() ===")
print(f"   isinstance(age, int): {isinstance(age, int)}")
print(f"   isinstance(height, float): {isinstance(height, float)}")
print(f"   isinstance(name, str): {isinstance(name, str)}")
print(f"   isinstance(is_student, bool): {isinstance(is_student, bool)}")

