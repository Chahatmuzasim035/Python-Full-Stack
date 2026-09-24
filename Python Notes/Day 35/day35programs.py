
#1. Basic Shallow Copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print("Original:", original)
print("Shallow Copy:", shallow)


import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print("Original:", original)
print("Deep Copy:", deep)

shallow = original.copy()

shallow[0] = 100

print("Original:", original)
print("Copy:", shallow)





import copy

original = [[10, 20], [30, 40]]

deep = copy.deepcopy(original)

deep[0].append(50)

print("Original:", original)
print("Deep Copy:", deep)


import copy

original = [[10, 20], [30, 40]]

shallow = copy.copy(original)

shallow[0].append(50)

print("Original:", original)
print("Shallow Copy:", shallow)


import copy

student = {
    "name": "Chahat",
    "marks": {
        "Python": 90,
        "SQL": 85
    }
}

new_student = copy.deepcopy(student)

new_student["marks"]["Python"] = 100

print("Original:", student)
print("Deep Copy:", new_student)

import copy

student = {
    "name": "Chahat",
    "marks": {
        "Python": 90,
        "SQL": 85
    }
}

new_student = copy.copy(student)

new_student["marks"]["Python"] = 100

print("Original:", student)
print("Shallow Copy:", new_student)

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 10
deep[1][0] = 30

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)
