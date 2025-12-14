# Filename: src/L1/S2/01_variables.py

# Session 2: Variables & Data Types
# Practice: Creating and using variables

# Create variables with different data types
name = "Alice"
age = 25
height = 5.9
is_student = True

# Display the variables
print("=== Variable Examples ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is Student: {is_student}")

# Show variable types
print("\n=== Variable Types ===")
print(f"name is {type(name)}")
print(f"age is {type(age)}")
print(f"height is {type(height)}")
print(f"is_student is {type(is_student)}")

# Variables can be reassigned
print("\n=== Reassigning Variables ===")
age = 26  # Changed from 25 to 26
print(f"Updated age: {age}")

# Variables can change types (dynamic typing)
print("\n=== Dynamic Typing Example ===")
value = 25
print(f"value = {value}, type = {type(value)}")

value = "Now I'm a string!"
print(f"value = {value}, type = {type(value)}")

