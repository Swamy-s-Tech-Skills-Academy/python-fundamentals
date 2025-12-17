# Filename: src/L2/S7/02_writing_files.py

"""
✍️ Writing Text Files in Python
Level 2, Session 7: File Handling

This file demonstrates how to write and append to text files.
"""

import os

print("=" * 50)
print("✍️ WRITING TEXT FILES IN PYTHON")
print("=" * 50)


# ============================================================
# WRITE MODE ("w") - Creates new or OVERWRITES existing
# ============================================================
print("\n" + "=" * 50)
print("📝 WRITE MODE ('w') - Creates or Overwrites")
print("=" * 50)

# Create a new file with write mode
with open("greeting.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Python file handling.\n")
    file.write("This is the third line.\n")

print("✅ Created 'greeting.txt' with 3 lines")

# Read and display what we wrote
with open("greeting.txt", "r") as file:
    print("\nContents of greeting.txt:")
    print(file.read())


# ============================================================
# WARNING: Write mode ERASES existing content!
# ============================================================
print("=" * 50)
print("⚠️ WARNING: Write mode ERASES existing content!")
print("=" * 50)

# Let's see what happens when we open the same file in write mode
with open("greeting.txt", "w") as file:
    file.write("This replaced everything!\n")

print("Opened greeting.txt with 'w' mode again...")
with open("greeting.txt", "r") as file:
    print("\nContents now:")
    print(file.read())
print("😱 All previous content is GONE!")


# ============================================================
# APPEND MODE ("a") - Adds to existing content
# ============================================================
print("\n" + "=" * 50)
print("📎 APPEND MODE ('a') - Adds to End")
print("=" * 50)

# Start fresh
with open("log.txt", "w") as file:
    file.write("=== Application Log ===\n")

print("Created log.txt with header")

# Append multiple entries
entries = [
    "User logged in",
    "Data loaded successfully",
    "Report generated",
    "User logged out"
]

for entry in entries:
    with open("log.txt", "a") as file:
        file.write(f"• {entry}\n")
    print(f"✅ Appended: {entry}")

# Show final contents
print("\nFinal contents of log.txt:")
with open("log.txt", "r") as file:
    print(file.read())


# ============================================================
# WRITELINES() - Write multiple lines from a list
# ============================================================
print("=" * 50)
print("📋 WRITELINES() - Write Multiple Lines")
print("=" * 50)

# Note: writelines() does NOT add newlines automatically!
fruits = ["Apple", "Banana", "Cherry", "Date"]

# Wrong way - no newlines
with open("fruits_wrong.txt", "w") as file:
    file.writelines(fruits)

print("Using writelines() without \\n:")
with open("fruits_wrong.txt", "r") as file:
    print(f"  Result: {file.read()!r}")
print("  😅 All on one line!")

# Correct way - add newlines
fruits_with_newlines = [f"{fruit}\n" for fruit in fruits]

with open("fruits_correct.txt", "w") as file:
    file.writelines(fruits_with_newlines)

print("\nUsing writelines() WITH \\n:")
with open("fruits_correct.txt", "r") as file:
    print(file.read())


# ============================================================
# PRACTICAL EXAMPLE: Building a Simple Todo List
# ============================================================
print("=" * 50)
print("🎯 PRACTICAL EXAMPLE: Simple Todo Saver")
print("=" * 50)


def save_todos(filename, todos):
    """Save a list of todos to a file."""
    with open(filename, "w") as file:
        for todo in todos:
            file.write(f"[ ] {todo}\n")
    print(f"✅ Saved {len(todos)} todos to {filename}")


def add_todo(filename, todo):
    """Add a single todo to the file."""
    with open(filename, "a") as file:
        file.write(f"[ ] {todo}\n")
    print(f"✅ Added: {todo}")


def show_todos(filename):
    """Display all todos from the file."""
    try:
        with open(filename, "r") as file:
            print("\n📋 Your Todos:")
            print("-" * 30)
            for line in file:
                print(f"  {line.strip()}")
            print("-" * 30)
    except FileNotFoundError:
        print("No todos found!")


# Demo the todo system
my_todos = [
    "Learn Python file handling",
    "Practice writing code",
    "Build a project"
]

save_todos("todos.txt", my_todos)
add_todo("todos.txt", "Review and celebrate!")
show_todos("todos.txt")


# ============================================================
# COMPARISON: Write vs Append
# ============================================================
print("\n" + "=" * 50)
print("📊 COMPARISON: Write ('w') vs Append ('a')")
print("=" * 50)

print("""
| Mode | Symbol | File Exists?          | File Doesn't Exist? |
|------|--------|----------------------|---------------------|
| Write| 'w'    | ERASES and writes    | Creates new file    |
| Append| 'a'   | Adds to end          | Creates new file    |

💡 Key Insight:
   - Use 'w' when you want to START FRESH
   - Use 'a' when you want to ADD MORE
""")


# ============================================================
# BEST PRACTICE: Always use 'with' statement
# ============================================================
print("=" * 50)
print("✅ BEST PRACTICE: Always use 'with'")
print("=" * 50)

print("""
❌ AVOID (manual close):
    file = open("data.txt", "w")
    file.write("content")
    file.close()  # Easy to forget!

✅ USE (context manager):
    with open("data.txt", "w") as file:
        file.write("content")
    # Automatically closed!

Why? The 'with' statement:
• Automatically closes the file
• Closes even if errors occur
• Cleaner, safer code
""")


# ============================================================
# Cleanup
# ============================================================
print("=" * 50)
print("🧹 Cleaning up test files...")
print("=" * 50)

test_files = [
    "greeting.txt", "log.txt", "fruits_wrong.txt",
    "fruits_correct.txt", "todos.txt"
]

for filename in test_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  Removed: {filename}")

print("\n✨ All test files cleaned up!")
