# Filename: src/L1/S3/02_comparisons.py

print("=== Comparison Operators Demo ===\n")

# Basic comparisons
x, y = 10, 5
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y:  {x > y}")
print(f"x < y:  {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

print("\n=== Chained Comparisons ===\n")

# Range checking
age = 25
print(f"age = {age}")
print(f"Is age between 18 and 65? {18 <= age <= 65}")

score = 75
print(f"score = {score}")
print(f"Is score between 70 and 80? {70 <= score <= 80}")

print("\n=== Practical Grade Example ===\n")

# Simple grade checker
test_score = int(input("Enter your test score (0-100): "))

print(f"\nYour score: {test_score}")
print(f"Is passing (>= 60)? {test_score >= 60}")
print(f"Is excellent (>= 90)? {test_score >= 90}")
print(f"Is in B range (80-89)? {80 <= test_score <= 89}")
