
# ==========================================
# PYTHON DAY 3 - PROGRAMS
# ==========================================


# ==========================================
# PROGRAM 1: COMMENTS
# ==========================================

# This is a single-line comment
print("Welcome to Python")


# ==========================================
# PROGRAM 2: SWAPPING USING TEMPORARY VARIABLE
# ==========================================

a = 10
b = 20

temp = a
a = b
b = temp

print(a, b)


# ==========================================
# PROGRAM 3: SWAPPING USING ARITHMETIC
# ==========================================

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a, b)


# ==========================================
# PROGRAM 4: PYTHONIC SWAPPING
# ==========================================

a = 10
b = 20

a, b = b, a

print(a, b)


# ==========================================
# PROGRAM 5: STRING
# ==========================================

name = "Python"

print(name)
print(name[0])


# ==========================================
# PROGRAM 6: NUMERIC DATA TYPES
# ==========================================

age = 23
price = 199.99
number = 4 + 5j

print(age)
print(price)
print(number)

print(type(age))
print(type(price))
print(type(number))


# ==========================================
# PROGRAM 7: LIST
# ==========================================

items = ["Shoes", "Shirt", "Watch"]

print(items)
print(items[0])

items.append("Bag")

print(items)


# ==========================================
# PROGRAM 8: TUPLE
# ==========================================

colors = ("Red", "Blue", "Green")

print(colors)
print(colors[1])


# ==========================================
# PROGRAM 9: SINGLE-ITEM TUPLE
# ==========================================

student = ("Raju",)

print(student)
print(type(student))


# ==========================================
# PROGRAM 10: RANGE
# ==========================================

print(list(range(5)))
print(list(range(2, 8)))
print(list(range(0, 10, 2)))


# ==========================================
# PROGRAM 11: TYPE CHECKING
# ==========================================

name = "Raju"
age = 23
marks = 97.5

print(type(name))
print(type(age))
print(type(marks))
