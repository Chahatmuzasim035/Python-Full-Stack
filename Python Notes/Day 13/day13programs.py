# DAY 13 - PYTHON NUMBER PROGRAMS USING LOOPS

# 1. Reverse a number
number = int(input("Enter a number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse:", reverse)


# 2. Palindrome using while loop
number = int(input("Enter a number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# 3. Palindrome using string
number = int(input("Enter a number: "))
text = str(number)

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# 4. Count even digits
number = int(input("Enter a number: "))
count = 0

for digit in str(number):
    if int(digit) % 2 == 0:
        count += 1

print("Number of even digits:", count)


# 5. Print factors
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)


# 6. Count factors
number = int(input("Enter a number: "))
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

print("Number of factors:", count)


# 7. Factorial
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)


# 8. Armstrong number for a 3-digit number
number = int(input("Enter a number: "))
original = number
total = 0

while number > 0:
    digit = number % 10
    total += digit ** 3
    number //= 10

if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 9. Continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 10. Break example
for i in range(1, 6):
    if i == 3:
        break
    print(i)


# 11. Sum of digits
number = int(input("Enter a number: "))
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits:", total)


# 12. Count digits
number = int(input("Enter a number: "))
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("Number of digits:", count)


# 13. Count odd digits
number = int(input("Enter a number: "))
count = 0

for digit in str(number):
    if int(digit) % 2 != 0:
        count += 1

print("Number of odd digits:", count)


# 14. Product of digits
number = int(input("Enter a number: "))

if number == 0:
    product = 0
else:
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10

print("Product of digits:", product)


# 15. Prime number using factor count
number = int(input("Enter a number: "))
factor_count = 0

for i in range(1, number + 1):
    if number % i == 0:
        factor_count += 1

if factor_count == 2:
    print("Prime number")
else:
    print("Not a prime number")