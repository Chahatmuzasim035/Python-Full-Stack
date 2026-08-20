# ============================================================
# DAY 18 - PYTHON MODULES AND OS OPERATIONS
# ============================================================

# ------------------------------------------------------------
# 1. IMPORTING A COMPLETE MODULE
# ------------------------------------------------------------

import math

print("1. Importing complete module")
print("Square root:", math.sqrt(64))
print("Factorial:", math.factorial(5))


# ------------------------------------------------------------
# 2. IMPORTING SPECIFIC FUNCTIONS
# ------------------------------------------------------------

from math import sqrt, factorial

print("\n2. Importing specific functions")
print("Square root:", sqrt(49))
print("Factorial:", factorial(4))


# ------------------------------------------------------------
# 3. IMPORTING MODULE USING AN ALIAS
# ------------------------------------------------------------

import math as m

print("\n3. Module alias")
print("PI:", m.pi)
print("Square root:", m.sqrt(81))


# ------------------------------------------------------------
# 4. USER-DEFINED MODULE CONCEPT
# ------------------------------------------------------------
# Normally these functions could be placed in another file.
# They are kept here so all Day 18 code is in one file.

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def greet(name):
    return "Hello, " + name


print("\n4. User-defined module concept")
print(greet("Student"))
print("Addition:", add(10, 5))
print("Multiplication:", multiply(4, 3))


# ------------------------------------------------------------
# 5. __name__ VARIABLE
# ------------------------------------------------------------

print("\n5. __name__ variable")
print("Value of __name__:", __name__)

if __name__ == "__main__":
    print("This program is running directly.")


# ------------------------------------------------------------
# 6. MATH MODULE
# ------------------------------------------------------------

print("\n6. Math module")

number = 36

print("Square root:", math.sqrt(number))
print("Power:", math.pow(2, 5))
print("Ceiling:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Factorial:", math.factorial(5))


# ------------------------------------------------------------
# 7. RANDOM MODULE
# ------------------------------------------------------------

import random

print("\n7. Random module")

print("Random number:", random.randint(1, 100))

items = ["Apple", "Mango", "Orange", "Banana"]

print("Random item:", random.choice(items))


# ------------------------------------------------------------
# 8. JSON MODULE
# ------------------------------------------------------------

import json

print("\n8. JSON module")

student = {
    "name": "Aarav",
    "age": 21,
    "course": "Python"
}

json_data = json.dumps(student)

print("JSON data:", json_data)

python_data = json.loads(json_data)

print("Name:", python_data["name"])
print("Course:", python_data["course"])


# ------------------------------------------------------------
# 9. OS MODULE - CURRENT DIRECTORY
# ------------------------------------------------------------

import os

print("\n9. Current working directory")

print(os.getcwd())


# ------------------------------------------------------------
# 10. CREATE A DIRECTORY
# ------------------------------------------------------------

print("\n10. Creating a directory")

folder = "Day18_Practice"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")
else:
    print("Folder already exists")


# ------------------------------------------------------------
# 11. CREATE A SUBDIRECTORY
# ------------------------------------------------------------

print("\n11. Creating a subdirectory")

sub_folder = os.path.join(folder, "Files")

if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
    print("Subfolder created")
else:
    print("Subfolder already exists")


# ------------------------------------------------------------
# 12. CREATE A FILE
# ------------------------------------------------------------

print("\n12. Creating a file")

file_path = os.path.join(sub_folder, "sample.txt")

with open(file_path, "w") as file:
    file.write("This file was created using Python.")

print("File created:", file_path)


# ------------------------------------------------------------
# 13. LIST FILES AND FOLDERS
# ------------------------------------------------------------

print("\n13. Directory contents")

if os.path.exists(folder):

    for item in os.listdir(folder):
        print(item)

else:
    print("Folder does not exist")


# ------------------------------------------------------------
# 14. DISPLAY FULL PATHS
# ------------------------------------------------------------

print("\n14. Full paths")

if os.path.exists(sub_folder):

    for item in os.listdir(sub_folder):
        full_path = os.path.join(sub_folder, item)
        print(full_path)


# ------------------------------------------------------------
# 15. READ THE CREATED FILE
# ------------------------------------------------------------

print("\n15. Reading file")

if os.path.exists(file_path):

    with open(file_path, "r") as file:
        content = file.read()

    print("File content:", content)


# ------------------------------------------------------------
# 16. DELETE A FILE
# ------------------------------------------------------------

print("\n16. Delete a file")

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted")
else:
    print("File not found")


# ------------------------------------------------------------
# 17. DELETE AN EMPTY SUBDIRECTORY
# ------------------------------------------------------------

print("\n17. Delete an empty subdirectory")

if os.path.exists(sub_folder):
    os.rmdir(sub_folder)
    print("Subfolder deleted")
else:
    print("Subfolder not found")


# ------------------------------------------------------------
# 18. DELETE A DIRECTORY
# ------------------------------------------------------------

print("\n18. Delete the main directory")

if os.path.exists(folder):
    os.rmdir(folder)
    print("Main folder deleted")
else:
    print("Main folder not found")


# ============================================================
# END OF DAY 18
# ============================================================