# ============================================================
# DAY 25 - POLYMORPHISM IN PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. SAME METHOD NAME - DIFFERENT BEHAVIOR
# ------------------------------------------------------------

class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


print("1. Same method name - different behavior")

for animal in (Dog(), Cat()):
    animal.speak()


# ------------------------------------------------------------
# 2. DUCK TYPING
# ------------------------------------------------------------

class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


def animal_sound(animal):
    animal.speak()


print("\n2. Duck Typing")

d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)


# ------------------------------------------------------------
# 3. OPERATOR OVERLOADING WITH BOOK
# ------------------------------------------------------------

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


print("\n3. Operator Overloading")

b1 = Book(100)
b2 = Book(200)

print("Total pages:", b1 + b2)


# ------------------------------------------------------------
# 4. METHOD OVERLOADING USING DEFAULT ARGUMENT
# ------------------------------------------------------------

class Greet:
    def hello(self, name=None):

        if name:
            print("Hello", name)
        else:
            print("Hello")


print("\n4. Method Overloading Simulation")

g = Greet()

g.hello()
g.hello("Student")


# ------------------------------------------------------------
# 5. METHOD OVERRIDING
# ------------------------------------------------------------

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


print("\n5. Method Overriding")

a = Animal()
d = Dog()

a.speak()
d.speak()


# ------------------------------------------------------------
# 6. SHOP BILLING
# ------------------------------------------------------------

class Shop:

    def calculate_bill(self, item1, item2=0):

        total = item1 + item2

        print(
            f"Total Bill (No Discount): ₹{total}"
        )


class SpecialCustomer(Shop):

    def calculate_bill(self, item1, item2=0):

        total = item1 + item2

        discount = total * 0.10

        final_amount = total - discount

        print(
            f"Total Bill after 10% discount: ₹{final_amount}"
        )


print("\n6. Shop Billing Example")

print("Normal Customer:")

s1 = Shop()

s1.calculate_bill(100)
s1.calculate_bill(100, 200)


print("\nSpecial Customer:")

s2 = SpecialCustomer()

s2.calculate_bill(100)
s2.calculate_bill(100, 200)


# ------------------------------------------------------------
# 7. OPERATOR OVERLOADING WITH STUDENT
# ------------------------------------------------------------

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


print("\n7. Student Operator Overloading")

s1 = Student(50)
s2 = Student(40)

print("Combined marks:", s1 + s2)


# ------------------------------------------------------------
# 8. BOOK - +, * AND __str__()
# ------------------------------------------------------------

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(
            self.pages + other.pages
        )

    def __mul__(self, other):
        return Book(
            self.pages * other.pages
        )

    def __str__(self):
        return str(self.pages)


print("\n8. Book Operator Overloading")

b = Book(100)
b1 = Book(200)
b2 = Book(300)

print(b + b1 + b2)
print(b * b1 * b2)


# ------------------------------------------------------------
# 9. INDIVIDUAL BOOK OPERATIONS
# ------------------------------------------------------------

print("\n9. Individual Book Operations")

book_a = Book(100)
book_b = Book(200)

result_add = book_a + book_b
result_mul = book_a * book_b

print("After addition:", result_add)
print("After multiplication:", result_mul)


# ------------------------------------------------------------
# 10. DIFFERENT OPERATORS WITH NORMAL DATA
# ------------------------------------------------------------

print("\n10. Operators with Different Data Types")

print(10 + 20)

print("A" + "B")

print([1, 2] + [3, 4])


# ------------------------------------------------------------
# 11. METHOD OVERLOADING USING *args
# ------------------------------------------------------------

class Calculator:

    def add(self, *numbers):

        total = 0

        for number in numbers:
            total += number

        return total


print("\n11. Method Overloading Simulation using *args")

calc = Calculator()

print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))


# ------------------------------------------------------------
# 12. SIMPLE POLYMORPHISM FUNCTION
# ------------------------------------------------------------

class Car:

    def move(self):
        print("Car is moving")


class Boat:

    def move(self):
        print("Boat is sailing")


class Plane:

    def move(self):
        print("Plane is flying")


def start_movement(vehicle):
    vehicle.move()


print("\n12. Polymorphism with Different Objects")

start_movement(Car())
start_movement(Boat())
start_movement(Plane())


# ============================================================
# END OF DAY 25
# ============================================================
