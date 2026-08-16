# DAY 16 - PYTHON LAMBDA, FILTER, MAP, REDUCE & OBJECT REFERENCES

# 1. Basic lambda
square = lambda x: x * x
print(square(6))


# 2. Lambda with two arguments
add = lambda a, b: a + b
print("Sum:", add(15, 25))


# 3. Lambda for even or odd
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(14))


# 4. Lambda for maximum
maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(18, 27))


# 5. Lambda for string length
get_length = lambda text: len(text)
print(get_length("Python"))


# 6. Sort tuples by marks
students = [
    ("Asha", 82),
    ("Ravi", 95),
    ("Kiran", 74),
    ("Meena", 88)
]

result = sorted(students, key=lambda student: student[1])
print(result)


# 7. Sort tuples by marks in descending order
result = sorted(students, key=lambda student: student[1], reverse=True)
print(result)


# 8. Sort tuples by name
result = sorted(students, key=lambda student: student[0])
print(result)


# 9. Sort dictionaries by marks
students = [
    {"name": "Asha", "marks": 82},
    {"name": "Ravi", "marks": 95},
    {"name": "Kiran", "marks": 74},
    {"name": "Meena", "marks": 88}
]

result = sorted(students, key=lambda student: student["marks"])
print(result)


# 10. Sort strings by length
names = ["Ravi", "Alexander", "John", "Sai"]
result = sorted(names, key=lambda name: len(name))
print(result)


# 11. Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 12. Filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# 13. Filter values greater than 50
values = [20, 65, 40, 90, 55, 10]
large_values = list(filter(lambda x: x > 50, values))
print(large_values)


# 14. Filter long words
words = ["cat", "python", "code", "programming", "AI"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)


# 15. Map - square numbers
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)


# 16. Map - uppercase names
names = ["asha", "ravi", "kiran"]
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)


# 17. Map - add 10
numbers = [5, 10, 15, 20]
updated = list(map(lambda x: x + 10, numbers))
print(updated)


# 18. Map - string lengths
words = ["python", "java", "sql"]
lengths = list(map(lambda word: len(word), words))
print(lengths)


# 19. Reduce - sum
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print("Total:", total)


# 20. Reduce - product
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)


# 21. Reduce - largest number
numbers = [12, 45, 7, 30, 25]
largest = reduce(lambda a, b: a if a > b else b, numbers)
print("Largest:", largest)


# 22. Call by object reference - mutable list
def add_value(data):
    data.append(100)

numbers = [10, 20, 30]
print("Before:", numbers)
add_value(numbers)
print("After:", numbers)


# 23. Reassignment does not change the original variable
def change_value(x):
    x = 100

number = 10
print("Before:", number)
change_value(number)
print("After:", number)


# 24. Reassignment of a list parameter
def replace_list(data):
    data = [100, 200]

numbers = [10, 20]
print("Before:", numbers)
replace_list(numbers)
print("After:", numbers)


# 25. Modify a dictionary inside a function
def update_profile(profile):
    profile["course"] = "Python"

student = {"name": "Chahat"}
print("Before:", student)
update_profile(student)
print("After:", student)


# 26. Modify a set inside a function
def add_item(items):
    items.add(50)

numbers = {10, 20, 30}
print("Before:", numbers)
add_item(numbers)
print("After:", numbers)