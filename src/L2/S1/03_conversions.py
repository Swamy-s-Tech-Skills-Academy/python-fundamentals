# Filename: src/L2/S1/03_conversions.py
# Session 1: Advanced Data Structures - Conversions

# List with duplicates
scores = [85, 90, 85, 92, 90, 88, 85]
print("Original scores:", scores)

# Convert to set to remove duplicates
unique_scores = set(scores)
print("Unique scores:", unique_scores)

# Convert back to list (sorted)
sorted_unique = sorted(list(unique_scores))
print("Sorted unique scores:", sorted_unique)

# List to tuple
fruits_list = ["apple", "banana", "orange"]
fruits_tuple = tuple(fruits_list)
print("Fruits tuple:", fruits_tuple)

# Tuple to list
coordinates = (10, 20, 30)
coordinates_list = list(coordinates)
coordinates_list.append(40)  # Can modify now
print("Coordinates list:", coordinates_list)

