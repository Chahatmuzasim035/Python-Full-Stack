# Python Exception Handling — Code Examples

# 1. Basic ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# 2. ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Please enter a valid number!")


# 3. IndexError
try:
    nums = [10, 20, 30]
    print(nums[5])
except IndexError:
    print("Index out of range!")


# 4. Multiple Exceptions
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("You can't divide by zero!")


# 5. FileNotFoundError
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found!")


# 6. try-except-else
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a number!")
else:
    print("You entered:", num)


# 7. try-except-finally
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error!")
finally:
    print("This will always execute.")


# 8. Catching any exception
try:
    a = int("hello")
except Exception as e:
    print("Something went wrong:", e)


# 9. KeyError
try:
    data = {"name": "Jani"}
    print(data["age"])
except KeyError:
    print("Key not found in dictionary!")


# 10. Function with exception handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"


print(divide(10, 0))
print(divide(10, 2))


# 11. Nested try-except
try:
    a = int(input("Enter a number: "))

    try:
        result = 10 / a
        print("Result:", result)
    except ZeroDivisionError:
        print("You can't divide by zero inside inner try block.")

except ValueError:
    print("Please enter a valid integer.")


# 12. try-except-else division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("Division successful!")
    print("Result is:", result)


# 13. try-except-else-finally
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
else:
    print("Division successful!")
    print("Result is:", result)
finally:
    print("Program has finished execution (with or without errors).")
