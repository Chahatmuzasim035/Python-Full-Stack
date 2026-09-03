# ============================================================
# DAY 29 - USER DEFINED MODULES
# ============================================================

# ------------------------------------------------------------
# Program 1: Simple function
# ------------------------------------------------------------

def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))


# ------------------------------------------------------------
# Program 2: Addition function
# ------------------------------------------------------------

def add(a, b):
    return a + b


print("Addition:", add(10, 20))


# ------------------------------------------------------------
# Program 3: Subtraction function
# ------------------------------------------------------------

def subtract(a, b):
    return a - b


print("Subtraction:", subtract(20, 10))


# ------------------------------------------------------------
# Program 4: Multiplication function
# ------------------------------------------------------------

def multiply(a, b):
    return a * b


print("Multiplication:", multiply(5, 4))


# ------------------------------------------------------------
# Program 5: Division function
# ------------------------------------------------------------

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"


print("Division:", divide(20, 5))


# ------------------------------------------------------------
# Program 6: Square function
# ------------------------------------------------------------

def square(n):
    return n * n


print("Square:", square(6))


# ------------------------------------------------------------
# Program 7: Cube function
# ------------------------------------------------------------

def cube(n):
    return n ** 3


print("Cube:", cube(4))


# ------------------------------------------------------------
# Program 8: Find maximum of two numbers
# ------------------------------------------------------------

def maximum(a, b):
    if a > b:
        return a
    return b


print("Maximum:", maximum(25, 40))


# ------------------------------------------------------------
# Program 9: Find minimum of two numbers
# ------------------------------------------------------------

def minimum(a, b):
    if a < b:
        return a
    return b


print("Minimum:", minimum(25, 40))


# ------------------------------------------------------------
# Program 10: Check even or odd
# ------------------------------------------------------------

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


print("Number is:", check_even_odd(15))


# ------------------------------------------------------------
# Program 11: Check positive, negative or zero
# ------------------------------------------------------------

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"


print("Number:", check_number(-10))


# ------------------------------------------------------------
# Program 12: Calculate area of circle
# ------------------------------------------------------------

PI = 3.14


def circle_area(radius):
    return PI * radius * radius


print("Area of circle:", circle_area(5))


# ------------------------------------------------------------
# Program 13: Calculate simple interest
# ------------------------------------------------------------

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print("Simple Interest:", simple_interest(10000, 5, 2))


# ------------------------------------------------------------
# Program 14: Calculate factorial
# ------------------------------------------------------------

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("Factorial:", factorial(5))


# ------------------------------------------------------------
# Program 15: Check prime number
# ------------------------------------------------------------

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


number = 17

if is_prime(number):
    print(number, "is Prime")
else:
    print(number, "is Not Prime")


# ------------------------------------------------------------
# Program 16: Reverse a string
# ------------------------------------------------------------

def reverse_string(text):
    return text[::-1]


print("Reverse:", reverse_string("Python"))


# ------------------------------------------------------------
# Program 17: Check palindrome
# ------------------------------------------------------------

def is_palindrome(text):
    return text == text[::-1]


word = "madam"

if is_palindrome(word):
    print(word, "is Palindrome")
else:
    print(word, "is Not Palindrome")


# ------------------------------------------------------------
# Program 18: Find sum of list
# ------------------------------------------------------------

def list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


numbers = [10, 20, 30, 40]

print("List sum:", list_sum(numbers))


# ------------------------------------------------------------
# Program 19: Find largest element in list
# ------------------------------------------------------------

def largest(numbers):
    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


numbers = [12, 45, 23, 67, 34]

print("Largest:", largest(numbers))


# ------------------------------------------------------------
# Program 20: Find smallest element in list
# ------------------------------------------------------------

def smallest(numbers):
    smallest_number = numbers[0]

    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


numbers = [12, 45, 23, 67, 34]

print("Smallest:", smallest(numbers))


# ------------------------------------------------------------
# Program 21: Demonstrating variables and functions
# ------------------------------------------------------------

name = "Chahat"
age = 22


def student_details(name, age):
    print("Name:", name)
    print("Age:", age)


student_details(name, age)


# ------------------------------------------------------------
# Program 22: Using an alias for a function
# ------------------------------------------------------------

addition = add

print("Using function alias:", addition(50, 30))


# ------------------------------------------------------------
# Program 23: Multiple functions in one module
# ------------------------------------------------------------

def power(a, b):
    return a ** b


def remainder(a, b):
    return a % b


print("Power:", power(2, 5))
print("Remainder:", remainder(17, 5))


# ------------------------------------------------------------
# Program 24: Check __name__
# ------------------------------------------------------------

print("Current module name:", __name__)


# ------------------------------------------------------------
# Program 25: Main block
# ------------------------------------------------------------

def main():
    print("Program is running directly.")
    print(greet("Chahat"))
    print("10 + 20 =", add(10, 20))
    print("Square of 8 =", square(8))


if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# Program 26: Display Python module search paths
# ------------------------------------------------------------

import sys

print("\nPython Module Search Paths:")

for path in sys.path:
    print(path)


# ============================================================
# END OF DAY 29 PROGRAMS
# ============================================================