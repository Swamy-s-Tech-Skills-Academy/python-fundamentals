# Filename: src/L2/S3/02_reusable_functions.py
# Session 3: Functions - Reusability

# Function to print separator
def print_separator():
    print("-" * 40)

# Function to display header
def show_header(title):
    print_separator()
    print(title)
    print_separator()

# Use functions to organize output
show_header("Introduction")
print("Welcome to our program!")

show_header("Main Content")
print("This is the main section.")

show_header("Conclusion")
print("Thanks for using our program!")

