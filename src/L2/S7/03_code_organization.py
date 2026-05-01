# Filename: src/L2/S7/03_code_organization.py
# Session 6: Functions - Code Organization


def get_user_input():
    """Get and validate user input."""
    name = input("Enter name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Age must be a whole number. Setting age to -1.")
        age = -1  # validate_age() will reject this
    return name, age


def validate_age(age):
    """Check if age is valid."""
    return age >= 0 and age <= 120


def display_info(name, age):
    """Display user information."""
    print(f"\nName: {name}")
    print(f"Age: {age}")
    if age >= 18:
        print("Status: Adult")
    else:
        print("Status: Minor")


# Main program
def main():
    name, age = get_user_input()
    if validate_age(age):
        display_info(name, age)
    else:
        print("Invalid age!")


main()
