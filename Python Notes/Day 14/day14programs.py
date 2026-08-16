# DAY 13 - PYTHON PATTERN PROGRAMS
# Nested for-loop practice

# Q1. Increasing Star Triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Q2. Decreasing Star Triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q3. Increasing Number Triangle
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Q4. Same Number in Each Row
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

# Q5. Alphabet Triangle
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# Q6. Same Number Sequence in Every Row
for i in range(5):
    for j in range(1, 6):
        print(j, end="")
    print()

# Q7. Reverse Number Sequence in Every Row
for i in range(5):
    for j in range(5, 0, -1):
        print(j, end="")
    print()

# Q8. Continuous Number Triangle
number = 1
for i in range(1, 5):
    for j in range(i):
        print(number, end="")
        number += 1
    print()

# Q9. Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q10. Right-Aligned Star Triangle
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Q11. Pyramid Pattern
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Q12. Inverted Pyramid
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Q13. Diamond Pattern
n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Q14. Palindromic Number Pattern
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# Q15. Palindromic Number Pattern - 5 Rows
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# Q16. Hollow Rectangle
rows = 4
columns = 6
for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q17. Hollow Triangle
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Q18. Multiplication Tables from 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

# Q19. All Pairs from 1 to 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Q20. Same Number Pattern
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()