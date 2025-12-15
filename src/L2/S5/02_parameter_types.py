# Filename: src/L2/S5/02_parameter_types.py
# Session 5: Functions - Parameter Types

# Default parameters
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Uses default
greet("Bob", "Hi")                # Overrides default

# Keyword arguments
def introduce(name, age, city):
    print(f"{name}, {age}, from {city}")

introduce(name="Alice", age=25, city="NYC")
introduce(city="LA", name="Bob", age=30)  # Order doesn't matter

