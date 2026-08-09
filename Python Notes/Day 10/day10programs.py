# DAY 10 - PYTHON CONDITIONAL STATEMENTS

# 1. if statement
stock = 25
if stock > 0:
    print("Product is available in stock")


# 2. if statement with a false condition
stock = 0
if stock > 0:
    print("Product is available")

print("Checking completed")


# 3. if-else: stock check
stock = 5
if stock > 0:
    print("Product stock available")
else:
    print("Product stock not available")


# 4. Voting eligibility
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

print("End")


# 5. Even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 6. Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is largest")
else:
    print("Second number is largest")


# 7. if-elif-else: stock level
stock = int(input("Enter stock quantity: "))

if stock > 20:
    print("Stock is fully available")
elif stock > 0:
    print("Limited stock available")
else:
    print("Out of stock")


# 8. Grade decision
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs improvement")


# 9. Nested if: purchase eligibility
stock = int(input("Enter available stock: "))
premium_member = input("Are you a premium member? (yes/no): ").lower()

if stock > 0:
    print("Product is available")

    if premium_member == "yes":
        print("Priority delivery available")
    else:
        print("Standard delivery available")
else:
    print("Product is out of stock")


# 10. ATM minimum balance
balance = int(input("Enter account balance: "))

if balance >= 1000:
    print("Transaction allowed")
else:
    print("Minimum balance requirement not met")

print("Thank you")


# 11. Comparison operators
x = 10
y = 5

print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("x == y:", x == y)
print("x != y:", x != y)


# 12. Positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 13. Simple login validation
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown username")


# 14. Discount decision
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    print("20% discount")
elif amount >= 2500:
    print("10% discount")
else:
    print("No discount")


# 15. Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is largest")
elif b >= a and b >= c:
    print("Second number is largest")
else:
    print("Third number is largest")