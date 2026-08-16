# DAY 14 - PYTHON FUNCTIONS


# 1. Simple function
def greet():
    print("Hello, welcome to Python!")


greet()


# 2. Function with one parameter
def greet_user(name):
    print("Hello", name)


greet_user("Chahat")


# 3. Function with two parameters
def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)


# 4. Function returning a value
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print("Product:", result)


# 5. Check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


number = int(input("Enter a number: "))
print(check_even_odd(number))


# 6. Find the largest of two numbers
def largest(a, b):
    if a > b:
        return a
    return b


print("Largest:", largest(25, 18))


# 7. Find the largest of three numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


print("Largest:", largest_of_three(12, 35, 21))


# 8. Factorial using a function
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter a number: "))
print("Factorial:", factorial(number))


# 9. Prime number function
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")


# 10. Default argument
def welcome(name="User"):
    print("Welcome", name)


welcome()
welcome("Chahat")


# 11. Positional arguments
def subtract(a, b):
    return a - b


print(subtract(20, 5))


# 12. Keyword arguments
def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details(course="Python", name="Chahat", age=21)


# 13. *args
def calculate_sum(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Total:", calculate_sum(10, 20, 30, 40))


# 14. **kwargs
def show_details(**data):
    for key, value in data.items():
        print(key, ":", value)


show_details(name="Chahat", course="Python", level="Beginner")


# 15. Function for sum of digits
def sum_of_digits(number):
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))


# 16. Function for palindrome
def is_palindrome(number):
    text = str(number)
    return text == text[::-1]


number = int(input("Enter a number: "))

if is_palindrome(number):
    print("Palindrome")
else:
    print("Not a palindrome")


# 17. Local variable
def show_message():
    message = "This is a local variable"
    print(message)


show_message()


# 18. Reusable calculator function
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        return "Cannot divide by zero"
    else:
        return "Invalid operator"


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

print("Result:", calculator(x, y, op))