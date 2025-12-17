# Filename: src/L2/S7/01_reading_files.py

"""
📖 Reading Text Files in Python
Level 2, Session 7: File Handling

This file demonstrates different ways to read text files in Python.
"""

# First, let's create a sample file to read
print("=" * 50)
print("📁 CREATING A SAMPLE FILE")
print("=" * 50)

# Create a sample file for our examples
sample_content = """Python is amazing!
Learning to read files is essential.
This is line three.
And here's line four.
The final line of our sample file."""

with open("sample.txt", "w") as file:
    file.write(sample_content)
print("✅ Created 'sample.txt' for our examples\n")


# ============================================================
# METHOD 1: read() - Read entire file as one string
# ============================================================
print("=" * 50)
print("📖 METHOD 1: read() - Entire file as string")
print("=" * 50)

with open("sample.txt", "r") as file:
    content = file.read()
    print(f"Type: {type(content)}")
    print(f"Length: {len(content)} characters")
    print("\nContent:")
    print(content)
print()


# ============================================================
# METHOD 2: readline() - Read one line at a time
# ============================================================
print("=" * 50)
print("📖 METHOD 2: readline() - One line at a time")
print("=" * 50)

with open("sample.txt", "r") as file:
    print("Reading lines one by one:")
    line1 = file.readline()
    print(f"Line 1: {line1!r}")  # !r shows the \n character
    
    line2 = file.readline()
    print(f"Line 2: {line2!r}")
    
    line3 = file.readline()
    print(f"Line 3: {line3!r}")

print("\n💡 Notice the \\n (newline) at the end of each line!")
print()


# ============================================================
# METHOD 3: readlines() - All lines as a list
# ============================================================
print("=" * 50)
print("📖 METHOD 3: readlines() - All lines as list")
print("=" * 50)

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(f"Type: {type(lines)}")
    print(f"Number of lines: {len(lines)}")
    print("\nLines list:")
    for i, line in enumerate(lines, 1):
        print(f"  [{i}] {line!r}")
print()


# ============================================================
# METHOD 4: Iterate with for loop (Memory Efficient)
# ============================================================
print("=" * 50)
print("📖 METHOD 4: Iterate with for loop")
print("=" * 50)

print("Reading and processing each line:")
with open("sample.txt", "r") as file:
    line_number = 1
    for line in file:
        # .strip() removes the \n and any whitespace
        clean_line = line.strip()
        word_count = len(clean_line.split())
        print(f"Line {line_number}: {word_count} words - \"{clean_line}\"")
        line_number += 1
print()


# ============================================================
# PRACTICAL EXAMPLE: Reading and Processing Data
# ============================================================
print("=" * 50)
print("🎯 PRACTICAL EXAMPLE: Processing File Data")
print("=" * 50)

# Create a data file with numbers
numbers_content = """10
25
15
30
20
45
35"""

with open("numbers.txt", "w") as file:
    file.write(numbers_content)
print("Created 'numbers.txt' with some numbers\n")

# Read and process the numbers
with open("numbers.txt", "r") as file:
    numbers = []
    for line in file:
        num = int(line.strip())
        numbers.append(num)

print(f"Numbers read: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print()


# ============================================================
# TIP: Using strip() to clean lines
# ============================================================
print("=" * 50)
print("💡 TIP: Using strip() to clean lines")
print("=" * 50)

sample_with_spaces = """   Line with leading spaces
Line with trailing spaces   
   Line with both   """

with open("spaces.txt", "w") as file:
    file.write(sample_with_spaces)

print("Without strip():")
with open("spaces.txt", "r") as file:
    for line in file:
        print(f"  |{line}|")  # No strip - keeps newlines and spaces

print("\nWith strip():")
with open("spaces.txt", "r") as file:
    for line in file:
        print(f"  |{line.strip()}|")  # Clean!


# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 50)
print("📋 SUMMARY: Choosing the Right Method")
print("=" * 50)
print("""
| Method           | Use When                           |
|------------------|-----------------------------------|
| read()           | Need entire file as one string    |
| readline()       | Processing one line at a time     |
| readlines()      | Need a list of all lines          |
| for line in file | Large files (memory efficient)    |

💡 Best Practice: Use 'for line in file' for most cases!
""")

# Cleanup: remove the test files we created
import os
for filename in ["sample.txt", "numbers.txt", "spaces.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
print("🧹 Cleaned up test files")
