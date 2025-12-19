print("Multiplication Table (1-10)\n")

# Header row
print("    |", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print()

# Separator
print("-" * 45)

# Table body
for i in range(1, 11):
    print(f"{i:3} |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()