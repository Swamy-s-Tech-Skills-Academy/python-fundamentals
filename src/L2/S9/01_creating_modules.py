# Filename: src/L2/S9/01_creating_modules.py

"""
📦 Creating Your Own Modules
Level 2, Session 8: Modules Deep Dive & Code Organization

This file demonstrates how to create and use custom modules.
We'll create a string utility module and use it!
"""

import os
import shutil
import sys
import tempfile

demo_dir = tempfile.mkdtemp(prefix="pyfund_l2_s8_modules_")
module_path = os.path.join(demo_dir, "string_utils.py")

print("=" * 60)
print("📦 CREATING YOUR OWN MODULES")
print("=" * 60)


# ============================================================
# PART 1: A Module is Just a Python File!
# ============================================================
print("\n" + "=" * 60)
print("📚 PART 1: Understanding Modules")
print("=" * 60)

print("""
A module is simply a .py file containing code you can reuse!

You've already used built-in modules:
    import math
    import random
    from datetime import datetime

Now let's create our OWN module!
""")


# ============================================================
# PART 2: Creating a Module File
# ============================================================
print("=" * 60)
print("📝 PART 2: Creating a Module File")
print("=" * 60)

# Let's create a module file programmatically for this demo
module_code = '''"""
String utility functions - a custom module!

This module provides helpful functions for working with strings.
"""

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return text.title()

def count_words(text):
    """Count the number of words in text."""
    return len(text.split())

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def remove_vowels(text):
    """Remove all vowels from text."""
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

def is_palindrome(text):
    """Check if text is a palindrome (ignoring case and spaces)."""
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

def word_frequency(text):
    """Count frequency of each word."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
'''

# Write the module file
with open(module_path, "w") as f:
    f.write(module_code)

print("✅ Created 'string_utils.py' module!\n")
print("Module contents preview:")
print("-" * 40)
print(module_code[:500] + "...")
print("-" * 40)


# ============================================================
# PART 3: Importing Your Module
# ============================================================
print("\n" + "=" * 60)
print("📥 PART 3: Different Ways to Import")
print("=" * 60)

# Method 1: Import entire module
print("\n1️⃣ Method 1: Import entire module")
print("   import string_utils")

if demo_dir not in sys.path:
    sys.path.insert(0, demo_dir)
# Ensure a fresh import so this demo always reflects the newly generated module file.
sys.modules.pop("string_utils", None)
import string_utils

result = string_utils.capitalize_words("hello world python")
print(f"   string_utils.capitalize_words('hello world python')")
print(f"   Result: {result}")


# Method 2: Import specific functions
print("\n2️⃣ Method 2: Import specific functions")
print("   from string_utils import reverse_string, is_palindrome")

from string_utils import reverse_string, is_palindrome

print(f"   reverse_string('Python'): {reverse_string('Python')}")
print(f"   is_palindrome('radar'): {is_palindrome('radar')}")


# Method 3: Import with alias
print("\n3️⃣ Method 3: Import with alias")
print("   import string_utils as su")

import string_utils as su

print(f"   su.count_words('Python is awesome'): {su.count_words('Python is awesome')}")


# Method 4: Import all (not recommended)
print("\n4️⃣ Method 4: Import all (⚠️ avoid this)")
print("   from string_utils import *")
print("   Why avoid? Unclear where functions come from, potential naming conflicts")


# ============================================================
# PART 4: Using Our Module
# ============================================================
print("\n" + "=" * 60)
print("🎯 PART 4: Using Our String Utils Module")
print("=" * 60)

sample_text = "python programming is fun and python is powerful"

print(f"\nSample text: '{sample_text}'")
print("-" * 50)

# Capitalize words
print(f"Capitalized: {string_utils.capitalize_words(sample_text)}")

# Count words
print(f"Word count: {string_utils.count_words(sample_text)}")

# Reverse
print(f"Reversed: {string_utils.reverse_string(sample_text)}")

# Remove vowels
print(f"No vowels: {string_utils.remove_vowels(sample_text)}")

# Word frequency
print(f"Word frequency: {string_utils.word_frequency(sample_text)}")


# ============================================================
# PART 5: Practical Example - Text Analyzer
# ============================================================
print("\n" + "=" * 60)
print("🔬 PART 5: Practical Example - Text Analyzer")
print("=" * 60)


def analyze_text(text):
    """Analyze text using our string_utils module."""
    print("\n📊 TEXT ANALYSIS REPORT")
    print("=" * 40)
    print(f"Original text: {text[:50]}..." if len(text) > 50 else f"Original text: {text}")
    print("-" * 40)
    
    # Use our module functions
    print(f"📏 Word count: {string_utils.count_words(text)}")
    print(f"📏 Character count: {len(text)}")
    
    # Check for palindromes
    words = text.split()
    palindromes = [w for w in words if string_utils.is_palindrome(w) and len(w) > 1]
    print(f"🔄 Palindrome words: {palindromes if palindromes else 'None found'}")
    
    # Word frequency
    freq = string_utils.word_frequency(text)
    most_common = max(freq.items(), key=lambda x: x[1])
    print(f"📈 Most common word: '{most_common[0]}' ({most_common[1]} times)")
    
    # Title case version
    print(f"📝 Title case: {string_utils.capitalize_words(text[:30])}...")
    print("=" * 40)


# Test the analyzer
analyze_text("The quick brown fox jumps over the lazy dog and the fox was happy")
analyze_text("A man a plan a canal Panama")  # Famous palindrome sentence


# ============================================================
# BEST PRACTICES
# ============================================================
print("\n" + "=" * 60)
print("✅ MODULE BEST PRACTICES")
print("=" * 60)

print("""
1️⃣ USE DESCRIPTIVE MODULE NAMES
   ✅ string_utils.py, file_operations.py, data_processing.py
   ❌ stuff.py, my_code.py, temp.py

2️⃣ ADD A MODULE DOCSTRING
   '''
   This module provides utility functions for...
   '''

3️⃣ ADD FUNCTION DOCSTRINGS
   def my_function(param):
       '''Brief description of what it does.'''
       pass

4️⃣ PREFER SPECIFIC IMPORTS FOR CLARITY
   ✅ from string_utils import capitalize_words
   ⚠️ from string_utils import *

5️⃣ USE MODULE PREFIX FOR CLARITY
   ✅ string_utils.capitalize_words(text)
   
6️⃣ ONE PURPOSE PER MODULE
   Keep related functions together!
""")


# ============================================================
# Cleanup
# ============================================================
print("\n" + "=" * 60)
print("🧹 Cleaning up...")
print("=" * 60)

if os.path.exists(module_path):
    os.remove(module_path)
    print("Removed string_utils.py")

# Clean up the cached module files too
cache_dir = os.path.join(demo_dir, "__pycache__")
if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)
    print("Removed __pycache__/")

if os.path.exists(demo_dir):
    shutil.rmtree(demo_dir)
    print("Removed demo workspace")

if demo_dir in sys.path:
    sys.path.remove(demo_dir)

print("\n✨ Module creation lesson complete!")
