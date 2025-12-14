# Filename: src/L1/S5/03_fizzbuzz.py

"""
🎯 FizzBuzz Challenge

Classic programming challenge:
- Print numbers 1 to n
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both, print "FizzBuzz"
"""

print("=" * 40)
print("🎯 FIZZBUZZ CHALLENGE")
print("=" * 40)

n = int(input("\nEnter a number (try 30): "))

print(f"\nFizzBuzz from 1 to {n}:")
print("-" * 30)

for num in range(1, n + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print("-" * 30)
print("✨ Challenge complete!")

# Bonus: Pattern printing
print("\n" + "=" * 40)
print("🎨 PATTERN PRINTING")
print("=" * 40)

rows = 5

print("\n--- Right Triangle ---")
for i in range(1, rows + 1):
    print("*" * i)

print("\n--- Number Triangle ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n--- Pyramid ---")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
