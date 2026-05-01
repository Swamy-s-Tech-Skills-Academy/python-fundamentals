# Filename: src/L2/S9/03_multi_file_project.py

"""
🏗️ Building a Multi-File Project
Level 2, Session 8: Modules Deep Dive & Code Organization

This file demonstrates how to organize code across multiple files
for a real-world project structure.
"""

import os
import shutil
import sys
import tempfile

print("=" * 60)
print("🏗️ BUILDING A MULTI-FILE PROJECT")
print("=" * 60)


# ============================================================
# PART 1: Project Structure Overview
# ============================================================
print("\n" + "=" * 60)
print("📁 PART 1: Project Structure")
print("=" * 60)

print("""
For larger projects, split code into multiple files:

    my_calculator/
    ├── main.py           # Entry point - runs the program
    ├── operations.py     # Math operations
    ├── utils.py          # Utility/helper functions
    └── config.py         # Configuration settings

Let's build this project!
""")


# ============================================================
# PART 2: Create the Project Files
# ============================================================
print("=" * 60)
print("📝 PART 2: Creating Project Files")
print("=" * 60)

# Create project directory in OS temp space to avoid polluting the repo root
project_dir = os.path.join(tempfile.gettempdir(), "my_calculator")
if os.path.exists(project_dir):
    shutil.rmtree(project_dir)
os.makedirs(project_dir)
print(f"✅ Created directory: {project_dir}/")


# config.py - Configuration settings
config_code = '''"""
Configuration settings for the calculator application.
"""

# Application info
APP_NAME = "Super Calculator"
VERSION = "1.0.0"
AUTHOR = "Python Learner"

# Settings
DECIMAL_PLACES = 2
SHOW_HISTORY = True
MAX_HISTORY = 10
'''

with open(f"{project_dir}/config.py", "w") as f:
    f.write(config_code)
print("✅ Created: config.py (configuration settings)")


# operations.py - Math operations module
operations_code = '''"""
Mathematical operations module.

Contains all the calculation functions for the calculator.
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
    """Divide a by b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b

def power(base, exp):
    """Raise base to the power of exp."""
    return base ** exp

def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        return None
    return a % b


# Test the operations when run directly
if __name__ == "__main__":
    print("Testing operations module...")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")
    print(f"power(2, 8) = {power(2, 8)}")
    print(f"modulo(17, 5) = {modulo(17, 5)}")
    print("All operations work! ✅")
'''

with open(f"{project_dir}/operations.py", "w") as f:
    f.write(operations_code)
print("✅ Created: operations.py (math operations)")


# utils.py - Utility functions
utils_code = '''"""
Utility functions for the calculator application.

Contains helper functions for input/output and formatting.
"""

import config


def get_number(prompt):
    """Get a number from user input with validation."""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("❌ Please enter a valid number!")


def format_result(value):
    """Format a number result with configured decimal places."""
    if value is None:
        return "Error: undefined"
    return f"{value:.{config.DECIMAL_PLACES}f}"


def display_result(operation, a, b, result):
    """Display a calculation result in a nice format."""
    symbols = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷',
        'power': '^',
        'modulo': '%'
    }
    symbol = symbols.get(operation, '?')
    formatted = format_result(result)
    print(f"  📊 {a} {symbol} {b} = {formatted}")


def show_menu():
    """Display the calculator menu."""
    print("\\n" + "=" * 40)
    print(f"🧮 {config.APP_NAME} v{config.VERSION}")
    print("=" * 40)
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Power")
    print("  6. Modulo")
    print("  0. Exit")
    print("=" * 40)


def get_choice():
    """Get menu choice from user."""
    while True:
        try:
            choice = int(input("Enter your choice (0-6): "))
            if 0 <= choice <= 6:
                return choice
            print("❌ Please enter a number between 0 and 6")
        except ValueError:
            print("❌ Please enter a valid number")


# Test utilities when run directly
if __name__ == "__main__":
    print("Testing utils module...")
    print(f"format_result(3.14159) = {format_result(3.14159)}")
    print(f"format_result(None) = {format_result(None)}")
    show_menu()
    print("Utils work! ✅")
'''

with open(f"{project_dir}/utils.py", "w") as f:
    f.write(utils_code)
print("✅ Created: utils.py (utility functions)")


# main.py - Main entry point
main_code = '''"""
Super Calculator - Main Entry Point

This is the main file that runs the calculator application.
It imports and uses the other modules.
"""

import config
import operations
import utils


def calculate(choice, a, b):
    """Perform the calculation based on user choice."""
    if choice == 1:
        return operations.add(a, b), 'add'
    elif choice == 2:
        return operations.subtract(a, b), 'subtract'
    elif choice == 3:
        return operations.multiply(a, b), 'multiply'
    elif choice == 4:
        return operations.divide(a, b), 'divide'
    elif choice == 5:
        return operations.power(a, b), 'power'
    elif choice == 6:
        return operations.modulo(a, b), 'modulo'


def main():
    """Main function - entry point of the calculator."""
    print(f"\\n🚀 Welcome to {config.APP_NAME}!")
    print(f"   Version: {config.VERSION}")
    print(f"   Author: {config.AUTHOR}")
    
    history = []
    
    while True:
        utils.show_menu()
        choice = utils.get_choice()
        
        if choice == 0:
            print("\\n👋 Thanks for using Super Calculator!")
            if history and config.SHOW_HISTORY:
                print("\\n📜 Calculation History:")
                for h in history[-config.MAX_HISTORY:]:
                    print(f"   {h}")
            break
        
        # Get numbers
        a = utils.get_number("Enter first number: ")
        b = utils.get_number("Enter second number: ")
        
        # Calculate
        result, op_name = calculate(choice, a, b)
        
        # Display result
        utils.display_result(op_name, a, b, result)
        
        # Add to history
        formatted = utils.format_result(result)
        history.append(f"{a} {op_name} {b} = {formatted}")


if __name__ == "__main__":
    main()
'''

with open(f"{project_dir}/main.py", "w") as f:
    f.write(main_code)
print("✅ Created: main.py (main entry point)")


# ============================================================
# PART 3: Show the Project Structure
# ============================================================
print("\n" + "=" * 60)
print("📁 PART 3: Project Structure Created")
print("=" * 60)

print(f"""
{project_dir}/
├── config.py      - Settings and constants
├── operations.py  - Math calculation functions
├── utils.py       - Helper functions for I/O
└── main.py        - Entry point (run this!)

To run the calculator:
    cd {project_dir}
    python main.py
""")


# ============================================================
# PART 4: Demonstrate Imports
# ============================================================
print("=" * 60)
print("🔗 PART 4: How the Files Connect")
print("=" * 60)

print("""
File Relationships:
                                    
    ┌─────────────┐
    │   main.py   │  ← Entry point
    └─────────────┘
          │
          │ imports
          ▼
    ┌─────────────┬─────────────┬─────────────┐
    │   config    │  operations │    utils    │
    │   .py       │    .py      │    .py      │
    └─────────────┴─────────────┴─────────────┘
          │                           │
          └───────────────────────────┘
                utils imports config

Import statements in each file:
• main.py:       import config, operations, utils
• utils.py:      import config
• operations.py: (no imports - standalone)
• config.py:     (no imports - just constants)
""")


# ============================================================
# PART 5: Best Practices for Multi-File Projects
# ============================================================
print("=" * 60)
print("✅ PART 5: Multi-File Project Best Practices")
print("=" * 60)

print("""
1️⃣ CLEAR RESPONSIBILITIES
   • config.py    → Settings only
   • operations.py → Business logic/calculations
   • utils.py     → Helper functions
   • main.py      → Program flow/entry point

2️⃣ MINIMAL DEPENDENCIES
   • Each module should be as independent as possible
   • Avoid circular imports (A imports B, B imports A)

3️⃣ USE __name__ == "__main__" 
   • Add test code to each module
   • Test modules independently

4️⃣ SINGLE ENTRY POINT
   • main.py is THE file to run
   • Clear starting point for anyone

5️⃣ DOCUMENT YOUR MODULES
   • Module docstrings explain purpose
   • Function docstrings explain usage
""")


# ============================================================
# PART 6: Testing Individual Modules
# ============================================================
print("=" * 60)
print("🧪 PART 6: Each Module Can Be Tested Alone")
print("=" * 60)

print("""
Because each module has `if __name__ == "__main__":`,
you can test them individually:

    # Test just the operations
    python operations.py
    
    # Test just the utilities  
    python utils.py
    
    # Run the full application
    python main.py

This makes debugging much easier!
""")

# Actually run the operations module test
print("Running operations.py test code:")
print("-" * 40)
sys.path.insert(0, project_dir)

# Manually run the test code (simulating direct execution)
import importlib.util
spec = importlib.util.spec_from_file_location("operations", f"{project_dir}/operations.py")
if spec is None:
    raise ImportError(f"Could not create module spec. Ensure {project_dir}/operations.py exists.")
if spec.loader is None:
    module_name = spec.name or "unknown module"
    module_origin = spec.origin or "unknown origin"
    raise ImportError(f"Could not load module '{module_name}' from {module_origin}")

ops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ops)

# Just demonstrate the functions work
print(f"add(5, 3) = {ops.add(5, 3)}")
print(f"multiply(6, 7) = {ops.multiply(6, 7)}")
print(f"divide(15, 3) = {ops.divide(15, 3)}")
print("-" * 40)


# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 60)
print("📋 SUMMARY")
print("=" * 60)

print("""
🏗️ Multi-File Project Structure:

1. Split code by RESPONSIBILITY
   • Each file has ONE job
   
2. Use IMPORTS to connect files
   • import module_name
   • from module_name import function
   
3. main.py is the ENTRY POINT
   • Has if __name__ == "__main__": main()
   • Imports and uses other modules
   
4. Test modules INDEPENDENTLY
   • Each module has its own test code
   
5. Keep DEPENDENCIES simple
   • Avoid circular imports
   • config.py has no dependencies
""")


# ============================================================
# Cleanup
# ============================================================
print("\n" + "=" * 60)
print("🧹 Cleanup")
print("=" * 60)

try:
    keep_project = input(f"\nKeep the '{project_dir}/' folder? (y/n): ").lower().strip()
except (EOFError, OSError):
    keep_project = "n"

if keep_project != 'y':
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)
        print(f"Removed {project_dir}/ folder")
else:
    print(f"""
✅ Kept {project_dir}/ folder!

To try it out:
    cd {project_dir}
    python main.py
""")

if project_dir in sys.path:
    sys.path.remove(project_dir)

print("\n✨ Multi-file project lesson complete!")
