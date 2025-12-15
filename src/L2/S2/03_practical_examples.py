# Filename: src/L2/S2/03_practical_examples.py
# Session 2: List Comprehensions - Practical Examples

# Process student scores
scores = [75, 85, 92, 68, 88, 95, 72]
high_scores = [score for score in scores if score >= 80]
print("High scores (>=80):", high_scores)

# Extract first letters
words = ["Python", "Programming", "Fun"]
first_letters = [word[0] for word in words]
print("First letters:", first_letters)

# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit:", fahrenheit)

# Remove duplicates and sort
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_sorted = sorted([n for n in set(numbers)])
print("Unique sorted:", unique_sorted)

