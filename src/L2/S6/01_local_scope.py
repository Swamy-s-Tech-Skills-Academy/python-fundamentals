# Filename: src/L2/S6/01_local_scope.py
# Session 6: Functions - Local Scope

def function_a():
    value = 10  # Local variable
    print(f"Function A: {value}")

def function_b():
    value = 20  # Different local variable
    print(f"Function B: {value}")

function_a()  # Function A: 10
function_b()  # Function B: 20

# value doesn't exist here
# print(value)  # Would cause error

