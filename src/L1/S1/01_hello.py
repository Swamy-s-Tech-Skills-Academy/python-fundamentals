# Filename: src/L1/S1/01_hello.py
# Session 1: Python Introduction & Environment Setup

import sys

if hasattr(sys.stdout, "reconfigure"):
    # Force UTF-8 so emoji/text samples run on common Windows terminals.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

print("Hello, World!")
print("Welcome to Python Fundamentals!")
print("This is Session 1")

# This is a single-line comment
print("\n💬 Comments help explain code")

"""
This is a multi-line comment. We'll learn more about these in future sessions.
"""
print("\n💬 Multi-line comments are useful for longer explanations")

print("\n👉 Programs run line by line, top to bottom — order matters.")
