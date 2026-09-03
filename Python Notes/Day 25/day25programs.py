# Day 26 – Python Inheritance
# All examples from the inheritance notes are collected in this single file.


# --------------------------------------------------
# 1. Single Inheritance
# --------------------------------------------------

class User:
    def login(self):
        print("Every user must log in")


class Manager(User):
    def manage_users(self):
        print("Manager can manage the users")


m = Manager()
m.login()
m.manage_users()


# --------------------------------------------------
# 2. Multiple Inheritance
# --------------------------------------------------

class Father:
    def dance(self):
        print("Dancing")


class Mother:
    def cook(self):
        print("Cooking")


class Child(Father, Mother):
    def play(self):
        print("Playing")


c = Child()
c.dance()
c.play()
c.cook()


# --------------------------------------------------
# 3. Multiple Inheritance – Full Stack Example
# --------------------------------------------------

class FrontendDev:
    def developfrontend(self):
        print("Develop with HTML, CSS, JS and React")


class BackendDev:
    def developbackend(self):
        print("Develop with Python, Flask or Django")


class FullstackDev(FrontendDev, BackendDev):
    def deploy(self):
        print("Deploy the full stack project on a cloud platform")


f = FullstackDev()
f.deploy()
f.developbackend()
f.developfrontend()


# --------------------------------------------------
# 4. Multiple Inheritance – Simple Example
# --------------------------------------------------

class A:
    def m1(self):
        print("I am m1() in class-A")


class B:
    def m2(self):
        print("I am m2() in class-B")


class C(A, B):
    def m3(self):
        print("I am m3() in class-C")


obj = C()
obj.m1()
obj.m2()
obj.m3()


# --------------------------------------------------
# 5. MRO – Method Conflict
# --------------------------------------------------

class A:
    def m1(self):
        print("I am m1 in class-A")


class B:
    def m1(self):
        print("I am m1 in class-B")


class C(B, A):
    def m1(self):
        print("I am m1 in class-C")


obj = C()
obj.m1()
print(C.__mro__)


# --------------------------------------------------
# 6. super() with Constructors
# --------------------------------------------------

class Employee:
    def __init__(self, ename, eid):
        self.ename = ename
        self.eid = eid


class ChildEmployee(Employee):
    def __init__(self, ename, eid, esal):
        super().__init__(ename, eid)
        self.esal = esal


employee = ChildEmployee("Rajesh", 102, 20000)
print(employee.ename)
print(employee.eid)
print(employee.esal)


# --------------------------------------------------
# 7. Single Inheritance – Animal Example
# --------------------------------------------------

class Animal:
    def sound(self):
        print("Animal is making sound!")


class Dog(Animal):
    def barking(self):
        print("Dog is barking!")


dog = Dog()
dog.barking()
dog.sound()

animal = Animal()
animal.sound()


# --------------------------------------------------
# 8. Multiple Inheritance – Skills
# --------------------------------------------------

class Father:
    def skill1(self):
        print("Father: Cooking")


class Mother:
    def skill2(self):
        print("Mother: Dancing")


class Child(Father, Mother):
    def skill3(self):
        print("Child: Singing")


child = Child()
child.skill1()
child.skill2()
child.skill3()


# --------------------------------------------------
# 9. Multiple Inheritance – IT Roles
# --------------------------------------------------

class Developer:
    def develop(self):
        print("Writes code")


class Tester:
    def test(self):
        print("Tests application")


class DevOpsEngineer(Developer, Tester):
    def deploy(self):
        print("Deploys the application")


engineer = DevOpsEngineer()
engineer.develop()
engineer.test()
engineer.deploy()


# --------------------------------------------------
# 10. Multiple Inheritance – Student Abilities
# --------------------------------------------------

class Sports:
    def play(self):
        print("Plays Football")


class Music:
    def sing(self):
        print("Sings Songs")


class Student(Sports, Music):
    def study(self):
        print("Studies Python")


student = Student()
student.play()
student.sing()
student.study()


# --------------------------------------------------
# 11. MRO – Basic Conflict Example
# --------------------------------------------------

class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.show()
print(C.__mro__)


# --------------------------------------------------
# 12. Diamond Problem
# --------------------------------------------------

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


d = D()
d.show()
print(D.__mro__)


# --------------------------------------------------
# 13. Multilevel Inheritance
# --------------------------------------------------

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class BabyDog(Dog):
    def cry(self):
        print("Crying")


baby = BabyDog()
baby.cry()
baby.bark()
baby.eat()


# --------------------------------------------------
# 14. Multilevel Inheritance – Employee Example
# --------------------------------------------------

class Employee:
    def work(self):
        print("Working")


class Developer(Employee):
    def code(self):
        print("Coding")


class Intern(Developer):
    def learn(self):
        print("Learning")


intern = Intern()
intern.learn()
intern.code()
intern.work()


# --------------------------------------------------
# 15. Hierarchical Inheritance
# --------------------------------------------------

class Vehicle:
    def fuel_type(self):
        print("Uses fuel or battery")


class Car(Vehicle):
    def drive(self):
        print("Driving the car")


class Bike(Vehicle):
    def ride(self):
        print("Riding the bike")


car = Car()
car.fuel_type()
car.drive()

bike = Bike()
bike.fuel_type()
bike.ride()


# --------------------------------------------------
# 16. Hierarchical Inheritance – Animal Example
# --------------------------------------------------

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat makes a meow sound")


cat = Cat()
cat.meow()
cat.eat()

dog = Dog()
dog.bark()
dog.eat()


# --------------------------------------------------
# 17. Hybrid Inheritance
# --------------------------------------------------

class A:
    def m1(self):
        print("m1 method in A class")


class B(A):
    def m2(self):
        print("m2 method in B class")


class C(A):
    def m3(self):
        print("m3 method in C class")


class D(B, C):
    def m4(self):
        print("m4 method in D class")


d = D()
d.m4()
d.m2()


# --------------------------------------------------
# 18. Parent and Child – Method Overriding + super()
# --------------------------------------------------

class Parent:
    college = "rice"

    def show(self):
        self.a = 200
        print("Hello from Parent")

    def get_name(self):
        return self.a


class Child(Parent):
    college = "pace"

    def show(self):
        self.a = 10
        print("I am a in Child:", self.a)
        print("Hello from Child")

        super().show()
        print("a from super class:", super().get_name())

        print(self.college)
        print(Parent.college)


child = Child()
child.show()
print(child.a)


# --------------------------------------------------
# 19. Docstring
# --------------------------------------------------

def greet(name):
    """This function greets the person with the provided name."""
    print("Hello,", name)


print(greet.__doc__)
greet("Jani")


# --------------------------------------------------
# 20. super() – Parent Constructor
# --------------------------------------------------

class Parent:
    def __init__(self):
        print("Parent constructor called")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor called")


child = Child()


# --------------------------------------------------
# 21. super() – Parent Method
# --------------------------------------------------

class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        super().show()
        print("Child method")


child = Child()
child.show()


# --------------------------------------------------
# 22. super() – Employee and Manager
# --------------------------------------------------

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def show(self):
        super().show()
        print("Department:", self.department)


manager = Manager("Jani", "IT")
manager.show()


# --------------------------------------------------
# 23. Hybrid Inheritance – College Student
# --------------------------------------------------

class Person:
    def display(self):
        print("I am a person.")


class Student(Person):
    def show(self):
        print("I am a student.")


class Sports:
    def play(self):
        print("I play sports.")


class CollegeStudent(Student, Sports):
    def college_info(self):
        print("I am a college student.")


college_student = CollegeStudent()
college_student.display()
college_student.show()
college_student.play()
college_student.college_info()


# --------------------------------------------------
# 24. Hybrid Inheritance – Employee System
# --------------------------------------------------

class Person:
    def personal_info(self):
        print("I am a person.")


class Employee(Person):
    def employee_info(self):
        print("I am an employee.")


class Trainer:
    def trainer_info(self):
        print("I am a trainer.")


class Programmer(Employee, Trainer):
    def programmer_info(self):
        print("I am a programmer.")


programmer = Programmer()
programmer.personal_info()
programmer.employee_info()
programmer.trainer_info()
programmer.programmer_info()
