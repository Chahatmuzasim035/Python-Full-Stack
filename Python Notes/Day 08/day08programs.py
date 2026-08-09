# DAY 8 - PYTHON LISTS AND TUPLES


# =========================
# LISTS
# =========================

# 1. Creating lists
numbers = [10, 20, 30]
names = ["Ravi", "Teja", "Ankit"]
mixed = [10, "Python", 5.5, True]

print(numbers)
print(names)
print(mixed)


# 2. List concatenation
first = [1, 2]
second = [3, 4]
print(first + second)


# 3. List repetition
print([1, 2] * 3)


# 4. List indexing
data = [10, 20, 30, 40]
print("First:", data[0])
print("Last:", data[-1])


# 5. List slicing
values = [10, 20, 30, 40, 50]
print("Middle:", values[1:4])
print("Reversed:", values[::-1])


# 6. List membership
print(20 in values)
print(100 not in values)


# 7. Built-in list functions
scores = [10, 25, 15, 30]

print("Length:", len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
print("Total:", sum(scores))
print("Sorted:", sorted(scores))


# 8. Adding elements
items = [10, 20]

items.append(30)
print("After append:", items)

items.extend([40, 50])
print("After extend:", items)

items.insert(1, 15)
print("After insert:", items)


# 9. Removing elements
items.remove(15)
print("After remove:", items)

removed = items.pop()
print("Removed:", removed)
print("After pop:", items)

items.clear()
print("After clear:", items)


# 10. Searching in a list
data = [10, 20, 10, 30, 10]

print("Index of 20:", data.index(20))
print("Count of 10:", data.count(10))


# 11. Sorting and reversing
numbers = [5, 2, 8, 1, 4]

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

new_sorted = sorted(numbers)
print("New sorted list:", new_sorted)


# 12. Copying a list
original = [10, 20, 30]
duplicate = original.copy()

duplicate.append(40)

print("Original:", original)
print("Copy:", duplicate)


# 13. Nested lists
matrix = [[1, 2], [3, 4]]

print("First row:", matrix[0])
print("Element:", matrix[1][1])


# =========================
# TUPLES
# =========================

# 14. Creating tuples
numbers = (10, 20, 30)
names = ("Ravi", "Teja", "Ankit")
mixed = (10, "Python", 5.5, True)

print(numbers)
print(names)
print(mixed)


# 15. Empty and single-element tuples
empty = ()
single = (10,)

print("Empty tuple:", empty)
print("Single tuple:", single)


# 16. Tuple concatenation
a = (1, 2)
b = (3, 4)

print(a + b)


# 17. Tuple repetition
print((1, 2) * 3)


# 18. Tuple indexing
data = (10, 20, 30, 40)

print("First:", data[0])
print("Last:", data[-1])


# 19. Tuple slicing
data = (10, 20, 30, 40, 50)

print("Slice:", data[1:4])
print("Reverse:", data[::-1])


# 20. Tuple membership
print(20 in data)
print(100 not in data)


# 21. Built-in tuple functions
values = (10, 25, 15, 30)

print("Length:", len(values))
print("Maximum:", max(values))
print("Minimum:", min(values))
print("Total:", sum(values))
print("Sorted:", sorted(values))
print("Any:", any(values))
print("All:", all(values))


# 22. Tuple methods
data = (10, 20, 10, 30)

print("Count of 10:", data.count(10))
print("Index of 20:", data.index(20))


# 23. Tuple packing
packed = 10, 20, 30
print("Packed tuple:", packed)


# 24. Tuple unpacking
data = (10, 20, 30)
x, y, z = data

print(x)
print(y)
print(z)


# 25. Nested tuple
data = ((1, 2), (3, 4))

print("First nested tuple:", data[0])
print("Nested element:", data[1][1])


# 26. Tuple with a mutable object
data = (10, [20, 30], 40)

data[1].append(50)

print(data)


# 27. Demonstrating list mutability
items = [10, 20, 30]
items[0] = 100

print("Modified list:", items)


# 28. List vs tuple example
changing_data = [10, 20, 30]
fixed_data = (10, 20, 30)

changing_data.append(40)

print("Changing collection:", changing_data)
print("Fixed collection:", fixed_data)


# 29. Coordinates using tuple
location = (17.3850, 78.4867)
print("Location:", location)


# 30. Dimensions using tuple
dimensions = (10, 20, 5)
print("Dimensions:", dimensions)