# DAY 15 - PYTHON FUNCTIONS

# 1. Built-in functions
numbers = [8, 3, 12, 5]

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
print("Type:", type(numbers))
print("Absolute:", abs(-25))
print("Rounded:", round(4.678, 2))


# 2. User-defined function
def welcome():
    print("Welcome to Python")


welcome()


# 3. Function with a parameter
def greet(name):
    print("Hello", name)


greet("Chahat")


# 4. Function with two parameters
def add(a, b):
    return a + b


print("Sum:", add(15, 25))


# 5. Function with return value
def square(number):
    return number * number


result = square(6)
print("Square:", result)


# 6. Multiple return values
def student_info():
    return "Asha", 92


name, marks = student_info()
print("Name:", name)
print("Marks:", marks)


# 7. Positional arguments
def login(username, password):
    print("Username:", username)
    print("Password:", password)


login("user01", "pass123")


# 8. Default argument
def delivery_charge(charge=40):
    print("Delivery charge:", charge)


delivery_charge()
delivery_charge(75)


# 9. Keyword arguments
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)


employee(salary=45000, name="Ravi")


# 10. *args
def total_bill(*prices):
    return sum(prices)


print("Total bill:", total_bill(500, 750, 1200))


# 11. Display *args values
def show_numbers(*numbers):
    print("Values:", numbers)


show_numbers(10, 20, 30, 40)


# 12. **kwargs
def profile(**details):
    for key, value in details.items():
        print(key, ":", value)


profile(name="Chahat", age=21, city="Hyderabad")


# 13. Lambda function - square
square = lambda x: x * x

print("Square:", square(7))


# 14. Lambda function - larger number
larger = lambda a, b: a if a > b else b

print("Larger:", larger(18, 25))


# 15. Lambda function - even check
is_even = lambda number: number % 2 == 0

print("Even:", is_even(12))


# 16. Recursive factorial
def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)


print("Factorial:", factorial(5))


# 17. Recursive countdown
def countdown(number):
    if number == 0:
        print("Done!")
        return

    print(number)
    countdown(number - 1)


countdown(5)


# 18. Recursive Fibonacci
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print("Fibonacci:", fibonacci(7))


# 19. Function to calculate GST
def calculate_gst(amount):
    gst = amount * 0.18
    return gst


amount = float(input("Enter amount: "))
print("GST:", calculate_gst(amount))


# 20. Function to check palindrome
def is_palindrome(value):
    text = str(value)
    return text == text[::-1]


value = input("Enter a value: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not a palindrome")