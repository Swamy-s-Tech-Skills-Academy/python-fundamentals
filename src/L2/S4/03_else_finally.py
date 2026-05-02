# Filename: src/L2/S4/03_else_finally.py
# Session 4: Error Handling - else and finally

# Using else clause
try:
    number = int(input("Enter a number: "))
    result = number**2
except ValueError:
    print("Invalid input!")
else:
    print(f"Square of {number} is {result}")
    print("Calculation successful!")

# Using finally clause
error_message = None

try:
    with open("test.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    error_message = "File not found"
    print("File not found!")
finally:
    # with statement handles file closing; finally runs completion tasks.
    print("Cleaning up operation state...")
    if error_message:
        print(f"Status: {error_message}")
    print("This always runs, whether file exists or not!")
