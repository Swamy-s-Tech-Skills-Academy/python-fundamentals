# Filename: src/L2/S4/02_multiple_exceptions.py
# Session 4: Error Handling - Multiple Exceptions

# Handle different error types
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        print("Error: Both values must be numbers!")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

# Test the function
print(safe_divide(10, 2))    # Works: 5.0
print(safe_divide(10, 0))    # ZeroDivisionError handled
print(safe_divide("10", 2))   # TypeError handled

