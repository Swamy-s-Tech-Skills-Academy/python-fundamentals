# Filename: src/L2/S6/02_global_scope.py
# Session 6: Functions - Global Scope

# Global variable
name = "Alice"

def greet():
    # Can read global variable
    print(f"Hello, {name}!")

greet()  # Hello, Alice!

# Modifying global
count = 0

def increment():
    global count
    count = count + 1
    print(f"Count: {count}")

increment()  # Count: 1
increment()  # Count: 2
print(f"Final: {count}")  # Final: 2

