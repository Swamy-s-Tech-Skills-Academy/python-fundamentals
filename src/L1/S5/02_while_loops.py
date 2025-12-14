# Filename: src/L1/S5/02_while_loops.py

import random

print("=== While Loops Demo ===\n")

# Basic while loop
print("--- Basic Counter ---")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While with user input
print("\n--- Guessing Game ---")
secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10): "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# Loop with break and continue
print("\n--- Skip and Stop Demo ---")
print("Printing numbers 1-10, skipping 5, stopping at 8:")
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue  # Skip 5
    if num == 8:
        break     # Stop at 8
    print(num)

# While with else
print("\n--- While-Else Demo ---")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally!")
