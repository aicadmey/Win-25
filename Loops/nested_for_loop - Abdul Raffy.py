# Nested for loops.

# 1. Multiplication Table for Numbers 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()

# 2. Printing a Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# 3. Right-Angled Triangle of Stars
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 4. Inverted Triangle of Stars
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 5. Printing a Number Pyramid
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 6. Reversed Number Pyramid
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 7. Hollow Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 8. Multiplication Table Grid
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

# 9. Diamond Pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

# 10. Pascal's Triangle
n = 5
for i in range(n):
    number = 1
    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)
    print()
