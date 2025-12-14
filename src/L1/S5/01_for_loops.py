# Filename: src/L1/S5/01_for_loops.py

print("=== For Loops Demo ===\n")

# Basic counting
print("--- Counting 1 to 5 ---")
for i in range(1, 6):
    print(i)

# Sum of numbers
print("\n--- Sum of 1 to 10 ---")
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")

# Iterating over a string
print("\n--- Letters in 'Python' ---")
for letter in "Python":
    print(f"Letter: {letter}")

# Using enumerate
print("\n--- Enumerate Demo ---")
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, 1):
    print(f"{idx}. {fruit}")

# Countdown
print("\n--- Countdown ---")
for i in range(5, 0, -1):
    print(i)
print("🚀 Blast off!")

# Multiplication table
print("\n--- 7 Times Table ---")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
