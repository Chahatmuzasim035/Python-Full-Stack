# DAY 17 - RECURSIVE FUNCTIONS & PASSING OBJECTS

# 1. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# 2. Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci term:", fibonacci(6))


# 3. Sum of natural numbers using recursion
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

print("Sum:", sum_natural(5))


# 4. Countdown using recursion
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# 5. Sum of digits using recursion
def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n // 10)

print("Digit sum:", digit_sum(12345))


# 6. Power using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print("Power:", power(2, 5))


# 7. Reverse a string using recursion
def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print("Reverse:", reverse_text("Python"))


# 8. Palindrome using recursion
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

print("Palindrome:", is_palindrome("madam"))


# 9. Immutable integer example
def modify_value(num):
    num += 10
    print("Inside:", num)

x = 5
modify_value(x)
print("Outside:", x)


# 10. Mutable list example
def modify_list(items):
    items.append(4)

numbers = [1, 2, 3]
print("Before:", numbers)
modify_list(numbers)
print("After:", numbers)


# 11. Modify a dictionary
def update_student(student):
    student["course"] = "Python"

data = {"name": "Chahat"}
update_student(data)
print(data)


# 12. Modify a set
def add_number(values):
    values.add(10)

numbers = {1, 2, 3}
add_number(numbers)
print(numbers)


# 13. Reassign an integer parameter
def change_number(num):
    num = 100

value = 20
change_number(value)
print("Original value:", value)


# 14. Reassign a list parameter
def replace_list(items):
    items = [100, 200]

numbers = [1, 2, 3]
replace_list(numbers)
print("Original list:", numbers)


# 15. Prevent list modification using a copy
def modify_copy(items):
    items = items[:]
    items.append(5)
    print("Inside:", items)

numbers = [1, 2, 3]
modify_copy(numbers)
print("Outside:", numbers)