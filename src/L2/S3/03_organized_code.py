# Filename: src/L2/S3/03_organized_code.py
# Session 3: Functions - Code Organization

# Function to calculate and display area
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Rectangle: {length} x {width} = {area}")

# Function to display results header
def show_results_header():
    print("=" * 40)
    print("AREA CALCULATIONS")
    print("=" * 40)

# Main program flow
show_results_header()
calculate_rectangle_area(5, 3)
calculate_rectangle_area(7, 4)
calculate_rectangle_area(10, 2)

