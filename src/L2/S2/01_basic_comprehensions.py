# Filename: src/L2/S2/01_basic_comprehensions.py
# Session 2: List Comprehensions - Basics

# Create list of numbers 0-9
numbers = [x for x in range(10)]
print("Numbers 0-9:", numbers)

# Square each number
squares = [x ** 2 for x in range(1, 11)]
print("Squares 1-10:", squares)

# Double each number
doubled = [x * 2 for x in range(5)]
print("Doubled 0-4:", doubled)

# Convert strings to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print("Uppercase words:", uppercase)

