# DAY 12 - PYTHON LOOP CONTROL
# Rewritten practice programs for GitHub.

# 1. FOR LOOP WITH ELSE - SEARCH
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Target found:", number)
        break
else:
    print("Target was not found")


# 2. FOR LOOP WITH ELSE - NOT FOUND
numbers = [10, 20, 30, 40]
target = 100

for number in numbers:
    if number == target:
        print("Target found")
        break
else:
    print("Target not present")


# 3. NOTIFICATIONS CHECK
notifications = [0, 0, 0, 0]

for notification in notifications:
    if notification == 1:
        print("You have an unread notification")
        break
else:
    print("All notifications are read")


# 4. BREAK - STOP AT A NUMBER
for number in range(1, 11):
    if number == 6:
        break
    print(number)


# 5. BREAK - SEARCH A LIST
values = [3, 8, 12, 17, 21]
target = 12

for value in values:
    if value == target:
        print("Found:", value)
        break


# 6. CONTINUE - PRINT ODD NUMBERS
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


# 7. CONTINUE - SKIP NEGATIVE VALUES
numbers = [-5, 10, -2, 8, 0, 15]

for number in numbers:
    if number < 0:
        continue
    print(number)


# 8. CONTINUE - SKIP MULTIPLES OF 3
for number in range(1, 16):
    if number % 3 == 0:
        continue
    print(number)


# 9. WHILE LOOP WITH ELSE
count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")


# 10. WHILE LOOP WITH BREAK
count = 1

while count <= 10:
    if count == 6:
        break
    print(count)
    count += 1


# 11. WHILE LOOP WITH ELSE AND BREAK
count = 1

while count <= 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("Completed without break")


# 12. OTP VERIFICATION
correct_otp = "7890"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_otp = input("Enter OTP: ")

    if entered_otp == correct_otp:
        print("OTP verified successfully")
        break

    print("Incorrect OTP. Try again.")
    attempts += 1
else:
    print("OTP expired. Request a new one")


# 13. BREAK VS CONTINUE
for number in range(1, 8):
    if number == 3:
        continue

    if number == 6:
        break

    print(number)


# 14. ASSERT - VALID CONDITION
age = 20

assert age >= 18, "Age must be at least 18"
print("Age condition is valid")


# 15. ASSERT WITH CUSTOM MESSAGE
marks = 75

assert 0 <= marks <= 100, "Marks must be between 0 and 100"
print("Valid marks:", marks)


# 16. ASSERT FOR POSITIVE NUMBER
number = 25

assert number > 0, "Number must be positive"
print("Positive number:", number)


# 17. SEARCH USING FOR-ELSE
names = ["Ravi", "Teja", "Ankit", "Priya"]
search_name = "Priya"

for name in names:
    if name == search_name:
        print("Name found:", name)
        break
else:
    print("Name not found")


# 18. FIND FIRST EVEN NUMBER
numbers = [7, 9, 13, 16, 21, 24]

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        break


# 19. PRINT VALUES EXCEPT ZERO
numbers = [10, 0, 20, 0, 30]

for number in numbers:
    if number == 0:
        continue
    print(number)


# 20. SIMPLE PASSWORD ATTEMPTS
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")
    attempts += 1
else:
    print("Account temporarily locked")