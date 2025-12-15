# Filename: src/L2/S3/01_basic_functions.py
# Session 3: Functions - Definition & Basics

# Simple greeting function
def greet():
    print("Hello! Welcome to Python.")
    print("Have a great day!")

# Call the function
print("First greeting:")
greet()

print("\nSecond greeting:")
greet()

# Function with logic
def show_menu():
    print("=" * 30)
    print("1. View items")
    print("2. Add item")
    print("3. Delete item")
    print("4. Exit")
    print("=" * 30)

show_menu()

