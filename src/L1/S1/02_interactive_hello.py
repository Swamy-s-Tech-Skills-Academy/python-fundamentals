# Filename: src/L1/S1/02_interactive_hello.py

# Interactive greeting script
print("=== Python Interactive Greeting ===")

# Get user input
name = input("What's your name? ")
age = input("How old are you? ")

# Display personalized message
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print("Nice to meet you!")

# Demonstrate built-in functions type() and help()
print("\n🔍 Let's explore Python's built-in functions:")
print(f"The name '{name}' is of type: {type(name)}")
print(f"The age '{age}' is of type: {type(age)}")

print("\n💡 Want to learn more about a function? Try help()!")
print("For example: help(print) shows documentation for print function")
print("(You can try this in the Python shell later!)")
