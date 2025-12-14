# Filename: src/L1/S1/bytecode_demo.py

# Session 1 - Advanced Example (Preview of what you'll learn)
# This shows what you can build after completing the course!

import dis
print("🚀 Advanced Python Preview")
print("=" * 50)

# Demonstrate Python's compilation process (from our lesson!)
print("\n🔍 Python Magic: Compilation & Interpretation Demo")
print("Let's see Python's bytecode in action!")


def greet():
    print("Hello World")


print("\n📄 Your Python Code:")
print("def greet():")
print("    print('Hello World')")

print("\n💾 Python's Bytecode (what the compiler creates):")
dis.dis(greet)

print("\n🎯 Cool, right? Python converted your code into bytecode!")
print("This is exactly what we learned about: Compilation → Bytecode → Interpretation")

print("\n" + "=" * 50)
print("🚀 Amazing! You've just seen Python's internal magic!")
print("This bytecode runs on the Python Virtual Machine.")
print("Keep learning, and you'll discover even more Python secrets! 🐍✨")
