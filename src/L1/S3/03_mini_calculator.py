# Filename: src/L1/S3/03_mini_calculator.py

print("=== Mini Calculator ===")
print("This calculator performs basic operations.\n")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform all operations
print(f"\n--- Results for {num1} and {num2} ---")
print(f"Addition:       {num1} + {num2} = {num1 + num2}")
print(f"Subtraction:    {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

# Handle division by zero
if num2 != 0:
    print(f"Division:       {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    print(f"Modulo:         {num1} % {num2} = {num1 % num2}")
else:
    print("Division:       Cannot divide by zero!")
    print("Floor Division: Cannot divide by zero!")
    print("Modulo:         Cannot divide by zero!")

print(f"Power:          {num1} ** {num2} = {num1 ** num2}")

print("\n✨ Calculation complete!")
