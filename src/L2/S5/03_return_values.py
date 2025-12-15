# Filename: src/L2/S5/03_return_values.py
# Session 5: Functions - Return Values

# Function that returns a value
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")

# Function that returns multiple values
def get_stats(numbers):
    if not numbers:
        return 0, 0, 0
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

scores = [85, 90, 92, 88, 95]
total, count, avg = get_stats(scores)
print(f"Total: {total}, Count: {count}, Average: {avg:.2f}")

# Function with docstring
def add(a, b):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - Sum of a and b
    """
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

