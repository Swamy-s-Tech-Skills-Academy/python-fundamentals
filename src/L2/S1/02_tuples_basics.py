# Filename: src/L2/S1/02_tuples_basics.py
# Session 1: Advanced Data Structures - Tuples

# Coordinate point (shouldn't change)
point_a = (10, 20)
point_b = (30, 40)

print("Point A:", point_a)
print("Point B:", point_b)

# Unpacking tuples
x, y = point_a
print(f"X coordinate: {x}, Y coordinate: {y}")

# Person information (immutable)
person = ("Alice", 25, "Engineer")
name, age, job = person
print(f"{name} is {age} years old and works as a {job}")

# Using tuple as dictionary key
locations = {
    (0, 0): "Origin",
    (10, 20): "Home",
    (30, 40): "Office"
}
print("Location at (10, 20):", locations[(10, 20)])

