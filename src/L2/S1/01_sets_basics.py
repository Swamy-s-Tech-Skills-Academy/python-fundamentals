# Filename: src/L2/S1/01_sets_basics.py
# Session 1: Advanced Data Structures - Sets

# Create a set of favorite colors
favorite_colors = {"blue", "green", "red", "blue", "yellow"}
print("Original colors:", favorite_colors)  # Duplicates removed!

# Add a new color
favorite_colors.add("purple")
print("After adding purple:", favorite_colors)

# Check if a color exists
if "blue" in favorite_colors:
    print("Blue is in my favorites!")

# Set operations
my_colors = {"blue", "green", "red"}
friend_colors = {"red", "yellow", "orange"}

# Colors we both like
common = my_colors & friend_colors
print("Common colors:", common)

# All unique colors
all_colors = my_colors | friend_colors
print("All colors:", all_colors)

