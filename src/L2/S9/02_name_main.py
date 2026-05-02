# Filename: src/L2/S9/02_name_main.py

"""
🔑 Understanding __name__ and __main__
Level 2, Session 8: Modules Deep Dive & Code Organization

This file demonstrates the important __name__ == "__main__" pattern
that controls when code runs.
"""

import os
import shutil
import sys
import tempfile

demo_dir = tempfile.mkdtemp(prefix="pyfund_l2_s9_name_main_")

print("=" * 60)
print("🔑 UNDERSTANDING __name__ AND __main__")
print("=" * 60)


# ============================================================
# PART 1: What is __name__?
# ============================================================
print("\n" + "=" * 60)
print("📚 PART 1: What is __name__?")
print("=" * 60)

print(f"""
Every Python file has a special variable called __name__.

Its value depends on HOW the file is run:

| How File Runs              | __name__ Value    |
|----------------------------|-------------------|
| python file.py (directly)  | "__main__"        |
| import file (as module)    | "file" (filename) |

Current file's __name__ = "{__name__}"
""")

# Show current __name__
print(f"Right now, __name__ = '{__name__}'")
if __name__ == "__main__":
    print("This means we're running the file DIRECTLY! ✅")
else:
    print("This means we're being IMPORTED as a module")


# ============================================================
# PART 2: The Problem This Solves
# ============================================================
print("\n" + "=" * 60)
print("❌ PART 2: The Problem Without __name__ Check")
print("=" * 60)

# Create a "bad" module that runs code on import
bad_module_code = '''"""
Example of a BAD module - runs code on import!
"""

def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"

def farewell(name):
    """Return a farewell."""
    return f"Goodbye, {name}!"

# ⚠️ This code runs EVERY TIME the module is imported!
print("=== Testing greetings module ===")
print(greet("World"))
print(farewell("World"))
print("=== Tests complete ===")
'''

# Write the bad module
with open(os.path.join(demo_dir, "bad_greetings.py"), "w") as f:
    f.write(bad_module_code)

print("Created 'bad_greetings.py' without __name__ protection...")
print("\nNow watch what happens when we import it:")
print("-" * 40)

if demo_dir not in sys.path:
    sys.path.insert(0, demo_dir)
# Clear cached module to ensure import behavior is demonstrated from fresh files
sys.modules.pop("bad_greetings", None)
import bad_greetings

print("-" * 40)
print("😱 Whoa! The test code ran just from importing!")
print("This is usually NOT what we want!")


# ============================================================
# PART 3: The Solution - if __name__ == "__main__"
# ============================================================
print("\n" + "=" * 60)
print("✅ PART 3: The Solution - if __name__ == '__main__'")
print("=" * 60)

# Create a "good" module with __name__ protection
good_module_code = '''"""
Example of a GOOD module - protected with __name__ check!
"""

def greet(name):
    """Return a greeting."""
    return f"Hello, {name}!"

def farewell(name):
    """Return a farewell."""
    return f"Goodbye, {name}!"

# ✅ This code ONLY runs when file is executed directly
if __name__ == "__main__":
    print("=== Testing greetings module ===")
    print(greet("World"))
    print(farewell("World"))
    print("=== Tests complete ===")
'''

# Write the good module
with open(os.path.join(demo_dir, "good_greetings.py"), "w") as f:
    f.write(good_module_code)

print("Created 'good_greetings.py' WITH __name__ protection...")
print("\nNow watch what happens when we import it:")
print("-" * 40)

# Clear cached module so the protected import example is evaluated freshly.
sys.modules.pop("good_greetings", None)
import good_greetings

print("(nothing printed!)")
print("-" * 40)
print("✅ Perfect! No unwanted output on import!")
print("\nBut we can still use the functions:")
print(f"  good_greetings.greet('Python') = '{good_greetings.greet('Python')}'")


# ============================================================
# PART 4: Practical Pattern - Module with Tests
# ============================================================
print("\n" + "=" * 60)
print("🎯 PART 4: Practical Pattern - Module with Tests")
print("=" * 60)

# Create a practical module
calculator_module = '''"""
Calculator module with built-in tests.

This module demonstrates the __name__ == "__main__" pattern
for including test code that only runs during direct execution.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b, returns None if b is zero."""
    if b == 0:
        return None
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent


# Test code - only runs when file is executed directly!
if __name__ == "__main__":
    print("=" * 40)
    print("🧪 Running Calculator Module Tests")
    print("=" * 40)
    
    # Test add
    assert add(2, 3) == 5, "add failed"
    print("✅ add(2, 3) = 5")
    
    # Test subtract
    assert subtract(10, 4) == 6, "subtract failed"
    print("✅ subtract(10, 4) = 6")
    
    # Test multiply
    assert multiply(5, 6) == 30, "multiply failed"
    print("✅ multiply(5, 6) = 30")
    
    # Test divide
    assert divide(15, 3) == 5, "divide failed"
    print("✅ divide(15, 3) = 5")
    
    # Test divide by zero
    assert divide(10, 0) is None, "divide by zero should return None"
    print("✅ divide(10, 0) = None")
    
    # Test power
    assert power(2, 3) == 8, "power failed"
    print("✅ power(2, 3) = 8")
    
    print("=" * 40)
    print("🎉 All tests passed!")
    print("=" * 40)
'''

# Write the module
with open(os.path.join(demo_dir, "calculator_module.py"), "w") as f:
    f.write(calculator_module)

print("Created 'calculator_module.py' with embedded tests\n")

print("When IMPORTED (like now):")
print("-" * 40)
# Clear cached module so this import uses the generated file for this run.
sys.modules.pop("calculator_module", None)
import calculator_module

print("(no output - tests didn't run)")
print("-" * 40)

print("\nWhen RUN DIRECTLY (python calculator_module.py):")
print("The test code would execute and show all tests passing!")


# ============================================================
# PART 5: Common Pattern - Main Function
# ============================================================
print("\n" + "=" * 60)
print("📋 PART 5: Common Pattern - main() Function")
print("=" * 60)

print("""
A common and clean pattern is to create a main() function:

    def main():
        '''Main entry point of the program.'''
        # Your program logic here
        print("Program running!")

    if __name__ == "__main__":
        main()

Why use this pattern?

1. ✅ Clear entry point - easy to find where program starts
2. ✅ Testable - you can call main() in tests
3. ✅ Clean - separates "what to do" from "when to do it"
4. ✅ Professional - industry standard pattern
""")


# ============================================================
# PART 6: Quick Reference
# ============================================================
print("\n" + "=" * 60)
print("📚 QUICK REFERENCE")
print("=" * 60)

print("""
┌────────────────────────────────────────────────────────┐
│ THE __name__ == "__main__" PATTERN                     │
├────────────────────────────────────────────────────────┤
│                                                        │
│  # Your module code (functions, classes)               │
│  def my_function():                                    │
│      pass                                              │
│                                                        │
│  # Protected code block                                │
│  if __name__ == "__main__":                            │
│      # This ONLY runs when file executed directly      │
│      # Perfect for:                                    │
│      #   - Tests                                       │
│      #   - Demo code                                   │
│      #   - Program entry point                         │
│      pass                                              │
│                                                        │
├────────────────────────────────────────────────────────┤
│ __name__ VALUES:                                       │
│   • "__main__" → file is run directly                  │
│   • "module_name" → file is imported                   │
└────────────────────────────────────────────────────────┘
""")


# ============================================================
# Cleanup
# ============================================================
print("=" * 60)
print("🧹 Cleaning up...")
print("=" * 60)

files_to_remove = [
    os.path.join(demo_dir, "bad_greetings.py"),
    os.path.join(demo_dir, "good_greetings.py"),
    os.path.join(demo_dir, "calculator_module.py"),
]
for filename in files_to_remove:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  Removed: {os.path.basename(filename)}")

cache_dir = os.path.join(demo_dir, "__pycache__")
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print("  Removed: __pycache__/")

if os.path.exists(demo_dir):
    shutil.rmtree(demo_dir)
    print("  Removed demo workspace")

if demo_dir in sys.path:
    sys.path.remove(demo_dir)

print("\n✨ __name__ and __main__ lesson complete!")
