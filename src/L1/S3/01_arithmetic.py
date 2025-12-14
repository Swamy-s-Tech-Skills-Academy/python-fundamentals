# Filename: src/L1/S3/01_arithmetic.py

print("=== Arithmetic Operators Demo ===\n")

# Basic arithmetic
a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Addition:       a + b = {a + b}")
print(f"Subtraction:    a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division:       a / b = {a / b}")
print(f"Floor Division: a // b = {a // b}")
print(f"Modulo:         a % b = {a % b}")
print(f"Exponentiation: a ** 2 = {a ** 2}")

print("\n=== Practical Examples ===\n")

# Check if even or odd
number = 17
remainder = number % 2
if remainder == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# Calculate square root
num = 144
sqrt = num ** 0.5
print(f"Square root of {num} is {sqrt}")

# Operator precedence
print("\n=== Operator Precedence ===\n")
print(f"2 + 3 * 4 = {2 + 3 * 4}")        # 14, not 20
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")    # 20
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")    # 512 (right-to-left!)
