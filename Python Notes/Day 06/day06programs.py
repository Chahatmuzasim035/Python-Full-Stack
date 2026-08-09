# DAY 6 - PYTHON INPUT AND OUTPUT FORMATTING

# =========================
# INPUT FORMATTING
# =========================

# 1. String input
name = input("Enter your name: ")
print("Name:", name)


# 2. Integer input
age = int(input("Enter your age: "))
print("Age:", age)


# 3. Float input
price = float(input("Enter the price: "))
print("Price:", price)


# 4. Space-separated strings
names = input("Enter names separated by spaces: ").split()
print("Names:", names)


# 5. Comma-separated values
items = input("Enter items separated by commas: ").split(",")
print("Items:", items)


# 6. List of integers
numbers = list(map(int, input("Enter integers: ").split()))
print("Integer list:", numbers)


# 7. List of floats
values = list(map(float, input("Enter decimal values: ").split()))
print("Float list:", values)


# 8. Tuple of integers
dimensions = tuple(map(int, input("Enter three dimensions: ").split()))
print("Tuple:", dimensions)


# 9. Set of integers
ids = set(map(int, input("Enter IDs: ").split()))
print("Unique IDs:", ids)


# 10. Dictionary input
# Use eval() only when the input is trusted.
profile = eval(input("Enter a trusted dictionary: "))
print("Profile:", profile)


# 11. Multiple values with unpacking
first, second = input("Enter two values: ").split()
print("First:", first)
print("Second:", second)


# =========================
# OUTPUT FORMATTING
# =========================

# 12. Basic print
print("Welcome to Python")


# 13. Multiple values
student = "Asha"
marks = 91
print("Student:", student, "Marks:", marks)


# 14. sep parameter
year = 2026
month = 8
day = 9
print(year, month, day, sep="-")


# 15. end parameter
print("Processing", end=" ")
print("completed")


# 16. Escape characters
print("First line\nSecond line")
print("Name:\tAsha")


# 17. Percent formatting
score = 87.456
print("Score: %.2f" % score)


# 18. f-string formatting
temperature = 36.789
print(f"Temperature: {temperature:.2f} C")


# 19. str.format()
amount = 1499.456
print("Amount: {:.2f}".format(amount))


# 20. Combining input and formatted output
product = input("Enter product: ")
cost = float(input("Enter cost: "))

print(f"Product: {product} | Cost: {cost:.2f}")