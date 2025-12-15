# Filename: src/L2/S2/02_filtered_comprehensions.py
# Session 2: List Comprehensions - Filtering

# Get only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers:", evens)

# Get words longer than 5 characters
words = ["apple", "banana", "cat", "elephant", "dog"]
long_words = [word for word in words if len(word) > 5]
print("Long words:", long_words)

# Square only even numbers
even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print("Squares of evens:", even_squares)

# Get positive scores
scores = [85, -10, 92, -5, 88, 0, 95]
positive = [score for score in scores if score > 0]
print("Positive scores:", positive)

