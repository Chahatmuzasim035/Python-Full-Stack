# Day 9 - Python Sets and Dictionaries
# Programs/examples based on the provided Day-9 Set & Dict PDF

# ============================================================
# SETS
# ============================================================

# 1. Creating and printing sets
numbers = {10, 20, 30}
names = {"Ravi", "Teja", "Ankit"}
mixed = {10, "Python", 5.5, True}

print(numbers)
print(names)
print(mixed)


# 2. Empty set
s = set()
print(s)


# 3. Set with duplicate values
data = {10, 20, 30, 20, 10}
print(data)


# 4. Membership operators
data = {10, 20, 30}

print(20 in data)
print(100 not in data)


# 5. Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


# 6. Intersection
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)


# 7. Difference
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)


# 8. Symmetric difference
a = {1, 2, 3}
b = {2, 3, 4}

print(a ^ b)


# 9. Subset
a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)


# 10. Superset
a = {1, 2, 3, 4}
b = {1, 2}

print(a >= b)


# 11. Built-in set functions
data = {10, 20, 5}

print(len(data))
print(max(data))
print(min(data))
print(sum(data))
print(sorted(data))
print(set("hello"))
print(any({0, 1}))
print(all({1, 2, 3}))


# 12. add()
s = {1, 2, 3}
s.add(10)
print(s)


# 13. update()
s = {1, 2, 3}
s.update([20, 30])
print(s)


# 14. remove()
s = {10, 20, 30}
s.remove(10)
print(s)


# 15. discard()
s = {10, 20, 30}
s.discard(10)
s.discard(100)
print(s)


# 16. pop()
s = {10, 20, 30}
removed = s.pop()
print("Removed:", removed)
print("Set:", s)


# 17. clear()
s = {10, 20, 30}
s.clear()
print(s)


# 18. copy()
s = {10, 20, 30}
copy_set = s.copy()
print(copy_set)


# 19. Set relation methods
a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


# 20. Subset, superset and disjoint methods
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}

print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))


# 21. Frozenset
data = frozenset({10, 20, 30})
print(data)


# 22. Practical set examples
unique_ids = {101, 102, 103}
available_sizes = {"S", "M", "L", "XL"}
visited_pages = {"Home", "Products", "Cart"}

print(unique_ids)
print(available_sizes)
print(visited_pages)


# ============================================================
# DICTIONARIES
# ============================================================

# 23. Creating a dictionary
student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python"
}

print(student)


# 24. Empty dictionary
data = {}
print(data)

data = dict()
print(data)


# 25. Dictionary with values
student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python"
}

print(student)


# 26. Creating dictionary using dict()
student = dict(
    id=101,
    name="Ravi",
    course="Python"
)

print(student)


# 27. Accessing dictionary values
student = {
    "name": "Ravi",
    "age": 22
}

print(student["name"])
print(student["age"])


# 28. Updating dictionary values
student = {
    "name": "Ravi",
    "age": 22
}

student["age"] = 23
print(student)


# 29. Adding new key-value pair
student = {"name": "Ravi"}

student["course"] = "Python"
print(student)


# 30. Removing dictionary item using del
student = {
    "name": "Ravi",
    "age": 22
}

del student["age"]
print(student)


# 31. Dictionary membership operators
student = {
    "name": "Ravi",
    "age": 22
}

print("name" in student)
print("course" not in student)


# 32. Built-in dictionary functions
d = {"b": 20, "a": 10, "c": 30}

print(len(d))
print(max(d))
print(min(d))
print(sorted(d))
print(dict())
print(any(d))
print(all(d))


# 33. get()
d = {
    "name": "Ravi",
    "age": 22
}

print(d.get("name"))


# 34. keys()
d = {
    "name": "Ravi",
    "age": 22
}

print(d.keys())


# 35. values()
d = {
    "name": "Ravi",
    "age": 22
}

print(d.values())


# 36. items()
d = {
    "name": "Ravi",
    "age": 22
}

print(d.items())


# 37. update()
d = {
    "name": "Ravi",
    "age": 22
}

d.update({"age": 25})
print(d)


# 38. setdefault()
d = {
    "name": "Ravi",
    "age": 22
}

print(d.setdefault("city", "Hyd"))
print(d)


# 39. pop()
d = {
    "name": "Ravi",
    "age": 22
}

removed = d.pop("age")
print("Removed:", removed)
print(d)


# 40. popitem()
d = {
    "name": "Ravi",
    "age": 22
}

removed = d.popitem()
print("Removed:", removed)
print(d)


# 41. clear()
d = {
    "name": "Ravi",
    "age": 22
}

d.clear()
print(d)


# 42. copy()
d = {
    "name": "Ravi",
    "age": 22
}

copy_dict = d.copy()
print(copy_dict)


# 43. fromkeys()
keys = ["a", "b"]
d = dict.fromkeys(keys, 0)

print(d)


# 44. Nested dictionary
students = {
    "s1": {"name": "Ravi", "age": 22},
    "s2": {"name": "Teja", "age": 21}
}

print(students["s1"]["name"])


# 45. Mutable values inside dictionaries
student = {
    "marks": [90, 85, 88]
}

student["marks"].append(95)
print(student)


# 46. Valid dictionary keys
data = {
    101: "Ravi",
    3.14: "Pi",
    True: "Yes",
    "name": "Python",
    (1, 2): "Tuple Key"
}

print(data)


# 47. Practical student dictionary
student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python"
}

print(student)


# 48. Practical product dictionary
product = {
    "name": "Laptop",
    "price": 50000
}

print(product)