# Import ABC and abstractmethod for creating an abstract class
from abc import ABC, abstractmethod


# Person is the parent/base class
# ABC means this class can contain abstract methods
class Person(ABC):

    def __init__(self, name, age):
        # Protected variables
        self._name = name
        self._age = age

    # Abstract method
    # Child classes must provide their own implementation
    @abstractmethod
    def get_role(self):
        pass

    # Common method used by all child classes
    def get_basic_info(self):
        return f"Name: {self._name}, Age: {self._age}"

    # Displays common information along with the role
    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"


# Student inherits from Person
# This is an example of inheritance
class Student(Person):

    def __init__(self, name, age, student_id, course):
        # super() calls the parent class constructor
        super().__init__(name, age)

        self._student_id = student_id
        self._course = course

    # Implementation of the abstract method
    def get_role(self):
        return "Student"

    # Student-specific information
    def get_student_info(self):
        return (
            f"{self.get_details()}, "
            f"Student ID: {self._student_id}, Course: {self._course}"
        )


# Professor is another child class of Person
class Professor(Person):

    def __init__(self, name, age, emp_id, department):
        # Calling parent constructor
        super().__init__(name, age)

        self._emp_id = emp_id
        self._department = department

    def get_role(self):
        return "Professor"

    # Professor-specific information
    def get_professor_info(self):
        return (
            f"{self.get_details()}, "
            f"Employee ID: {self._emp_id}, Department: {self._department}"
        )


# AdminStaff also inherits from Person
class AdminStaff(Person):

    def __init__(self, name, age, staff_id, designation):
        # Calling parent constructor
        super().__init__(name, age)

        self._staff_id = staff_id
        self._designation = designation

    def get_role(self):
        return "Admin Staff"

    # Admin staff-specific information
    def get_staff_info(self):
        return (
            f"{self.get_details()}, "
            f"Staff ID: {self._staff_id}, Designation: {self._designation}"
        )


# University class manages all registered people
class University:

    # Class variable
    # Same value is shared by all University objects
    university_name = "Codegnan University"

    def __init__(self):
        # Private list
        # Stores all Student, Professor and AdminStaff objects
        self.__people = []

    # Adds a person object to the private list
    def add_person(self, person: Person):
        self.__people.append(person)

    # Displays all registered people
    def display_all(self):
        if not self.__people:
            print("No people registered yet.")
        else:
            for person in self.__people:
                print(person.get_details())

    # Class method
    # Works with the class rather than a particular object
    @classmethod
    def get_university_name(cls):
        return cls.university_name

    # Static method
    # Does not require self or cls
    @staticmethod
    def welcome_message():
        return "Welcome to the University Management System"


# Program starts here

# Calling static method using class name
print(University.welcome_message())

# Calling class method using class name
print("University:", University.get_university_name())

# Creating University object
u = University()


# Menu-driven program
while True:

    print("\n--- University Menu ---")
    print("1. Register Student")
    print("2. Register Professor")
    print("3. Register Admin Staff")
    print("4. Display All People")
    print("0. Exit")

    ch = input("Choose an option: ")


    # Exit the program
    if ch == "0":
        print("Thank you! Exiting the system.")
        break


    # Register Student
    elif ch == "1":

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        student_id = input("Enter Student ID: ")
        course = input("Enter Course Name: ")

        # Creating Student object
        student = Student(name, age, student_id, course)

        # Adding Student object to University
        u.add_person(student)

        print("Student Registered Successfully!")


    # Register Professor
    elif ch == "2":

        name = input("Enter Professor Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")

        # Creating Professor object
        professor = Professor(name, age, emp_id, department)

        # Adding Professor object to University
        u.add_person(professor)

        print("Professor Registered Successfully!")


    # Register Admin Staff
    elif ch == "3":

        name = input("Enter Staff Name: ")
        age = int(input("Enter Age: "))
        staff_id = input("Enter Staff ID: ")
        designation = input("Enter Designation: ")

        # Creating AdminStaff object
        staff = AdminStaff(name, age, staff_id, designation)

        # Adding AdminStaff object to University
        u.add_person(staff)

        print("Admin Staff Registered Successfully!")


    # Display all registered people
    elif ch == "4":

        print("\n--- List of Registered People ---")
        u.display_all()


    # Handle invalid menu choices
    else:
        print("Invalid option. Please choose again.")