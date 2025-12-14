# Filename: src/L1/MP1/simple_calculator.py

"""
🧮 Simple Calculator - Mini Project 1
Level 1: Noob → Nerd

A command-line calculator demonstrating:
- User input and output
- Variables and data types
- Arithmetic operators
- Conditional statements
- Basic loop structure
"""


def show_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print("🧮 SIMPLE CALCULATOR 🧮")
    print("=" * 40)
    print("\nOperations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (**)")
    print("  6. Modulo (%)")
    print("  7. Quit")


def get_numbers():
    """Get two numbers from user with validation."""
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")


def calculate(choice, num1, num2):
    """Perform calculation based on user choice."""
    if choice == "1":
        return num1 + num2, "+"
    elif choice == "2":
        return num1 - num2, "-"
    elif choice == "3":
        return num1 * num2, "*"
    elif choice == "4":
        if num2 != 0:
            return num1 / num2, "/"
        else:
            print("❌ Error: Cannot divide by zero!")
            return None, None
    elif choice == "5":
        return num1 ** num2, "**"
    elif choice == "6":
        if num2 != 0:
            return num1 % num2, "%"
        else:
            print("❌ Error: Cannot calculate modulo with zero!")
            return None, None
    else:
        return None, None


def main():
    """Main calculator loop."""
    print("\n🎉 Welcome to Simple Calculator!")
    print("This calculator was built in Level 1, Phase A.")

    while True:
        show_menu()
        choice = input("\nEnter operation (1-7): ")

        # Check for quit
        if choice == "7":
            print("\n" + "=" * 40)
            print("👋 Thanks for using the calculator!")
            print("Happy coding! 🐍✨")
            print("=" * 40)
            break

        # Validate choice
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice! Please enter 1-7.")
            continue

        # Get numbers
        num1, num2 = get_numbers()

        # Calculate
        result, operation = calculate(choice, num1, num2)

        # Display result
        if result is not None:
            print("\n" + "-" * 40)
            print(f"✨ {num1} {operation} {num2} = {result}")
            print("-" * 40)


# Run the calculator
if __name__ == "__main__":
    main()
