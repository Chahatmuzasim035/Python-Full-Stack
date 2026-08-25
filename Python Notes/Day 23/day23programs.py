# ==========================================
# PYTHON OOP – DAY 24
# ==========================================


# 1. Non-Parameterized Constructor

class Student:

    def __init__(self):
        print("I am a non-parameterized constructor")


s1 = Student()
s2 = Student()


# 2. Object Identity

class Student:

    def __init__(self):
        print("Constructor executed")


s1 = Student()
print("Address of s1:", id(s1))

s2 = Student()
print("Address of s2:", id(s2))


# 3. Parameterized Constructor

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Chahat", 22)

print(s1.name)
print(s1.age)


# 4. Creating Multiple Objects

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Chahat", 22)
s2 = Student("Rahul", 21)

print(s1.name, s1.age)
print(s2.name, s2.age)


# 5. Using self

class Student:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Student Name:", self.name)


s1 = Student("Chahat")

s1.display_name()


# 6. Instance Method

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Chahat", 85)

s1.display_details()


# 7. Class Method

class Student:

    college = "ABC College"

    @classmethod
    def display_college(cls):
        print("College:", cls.college)


Student.display_college()


# 8. Static Method

class Student:

    @staticmethod
    def welcome():
        print("Welcome to Python OOP")


Student.welcome()


# 9. Constructor + Instance Method

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Chahat", 22)

s1.display_details()


# 10. Complete Example

class Student:

    college = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)

    @classmethod
    def display_college(cls):
        print("College:", cls.college)

    @staticmethod
    def welcome_message():
        print("Welcome to Student Management System")


s1 = Student("Chahat", 22)

s1.display_details()

Student.display_college()

Student.welcome_message()