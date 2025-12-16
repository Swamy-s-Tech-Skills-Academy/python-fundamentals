# Filename: src/L2/S4/03_else_finally.py
# Session 4: Error Handling - else and finally

# Using else clause
try:
    number = int(input("Enter a number: "))
    result = number ** 2
except ValueError:
    print("Invalid input!")
else:
    print(f"Square of {number} is {result}")
    print("Calculation successful!")

# Using finally clause
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs, whether file exists or not!")

