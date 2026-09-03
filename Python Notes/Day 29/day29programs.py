# DAY 19 - MODULES & USER-DEFINED MODULES
# Keep my_module.py and this file in the same folder.

# ------------------------------------------------------------
# FILE: my_module.py
# Create this as a separate file.
# ------------------------------------------------------------
#
# PI = 3.14159
#
# def greet(name):
#     return f"Hello, {name}!"
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     print(greet("Alice"))


# PROGRAM 1: Import a complete module
import my_module

print(my_module.greet("Chahat"))
print("PI:", my_module.PI)


# PROGRAM 2: Import one function
from my_module import greet

print(greet("Alice"))


# PROGRAM 3: Import multiple functions
from my_module import add, subtract

print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))


# PROGRAM 4: Module alias
import my_module as m

print(m.greet("Bob"))
print("Square:", m.square(7))


# PROGRAM 5: Function alias
from my_module import square as sq

print("Square:", sq(8))


# PROGRAM 6: Check __name__
print("__name__:", __name__)


# PROGRAM 7: Main execution block
def welcome():
    print("Welcome to Python Modules!")


if __name__ == "__main__":
    welcome()


# PROGRAM 8: Display module search path
import sys

for path in sys.path:
    print(path)


# PROGRAM 9: Add a custom module path
# Uncomment and replace with your actual folder path.
#
# import sys
# sys.path.append("C:/PythonModules")
# print(sys.path)


# PROGRAM 10: Use imported functions for calculations
a = 15
b = 5

print("Add:", my_module.add(a, b))
print("Subtract:", my_module.subtract(a, b))
print("Square:", my_module.square(a))
