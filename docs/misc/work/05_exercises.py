# Session 1 Exercises - Practice Files

# Exercise 1: Environment Test
import sys
print("🔧 Exercise 1: Testing Your Environment")
print("Python Version Check:")
print(f"Python version: {sys.version}")
print("✅ If you see this message, Python is working!")

# Exercise 2: Basic Calculator
print("\n🧮 Exercise 2: Simple Calculator")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to numbers and calculate
result = float(num1) + float(num2)
print(f"The sum of {num1} and {num2} is {result}")

# Exercise 3: Personal Profile
print("\n👤 Exercise 3: Create Your Profile")
print("Let's create your Python learner profile!")

name = input("Your name: ")
city = input("Your city: ")
favorite_color = input("Your favorite color: ")
python_goal = input("Why do you want to learn Python? ")

print(f"\n🌟 {name}'s Python Profile 🌟")
print(f"📍 Location: {city}")
print(f"🎨 Favorite color: {favorite_color}")
print(f"🎯 Python goal: {python_goal}")
print(f"🚀 Ready to start the Python journey!")

print("\n✨ Great job completing the exercises!")
