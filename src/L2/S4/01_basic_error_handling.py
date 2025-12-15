# Filename: src/L2/S4/01_basic_error_handling.py
# Session 4: Error Handling - Basics

# Handle ValueError
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number!")

# Handle ZeroDivisionError
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 / {number} = {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

