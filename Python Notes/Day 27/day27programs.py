# Data Abstraction Programs in Python

# ============================================================
# Program 1: Vehicle - Abstract Class and Abstract Methods
# ============================================================

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")


my_car = Car()
my_car.start_engine()
my_car.stop_engine()


# ============================================================
# Program 2: Bank - Different Implementations
# ============================================================

class Bank(ABC):

    @abstractmethod
    def loan_interest(self):
        pass


class SBI(Bank):

    def loan_interest(self):
        print("SBI interest rate is 8%")


class HDFC(Bank):

    def loan_interest(self):
        print("HDFC interest rate is 10%")


bank1 = SBI()
bank2 = HDFC()

bank1.loan_interest()
bank2.loan_interest()


# ============================================================
# Program 3: Abstract Class with a Concrete Method
# ============================================================

class BankWithServices(ABC):

    @abstractmethod
    def loan_interest(self):
        pass

    def bank_services(self):
        print("Common services: Net Banking, ATM, Mobile App")


class SBIWithServices(BankWithServices):

    def loan_interest(self):
        print("SBI interest rate is 8%")


class HDFCWithServices(BankWithServices):

    def loan_interest(self):
        print("HDFC interest rate is 10%")


sbi = SBIWithServices()
hdfc = HDFCWithServices()

sbi.loan_interest()
sbi.bank_services()

hdfc.loan_interest()
hdfc.bank_services()


# ============================================================
# Program 4: Abstraction Using Private Variable
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print("Salary is confidential.")


emp = Employee("Jani", 50000)
emp.show_info()

# Direct access is not recommended:
# print(emp.__salary)

# Name mangling can access the variable internally:
print("Salary using name mangling:", emp._Employee__salary)


# ============================================================
# Program 5: ATM Using Data Abstraction
# ============================================================

class ATM(ABC):

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def welcome(self):
        print("Welcome to Smart ATM!")


class UserAccount(ATM):

    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin
        self.__balance = balance

    def authenticate(self, pin_input):
        return self.__pin == pin_input

    def check_balance(self):
        print(f"Your current balance is: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()

    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")
        self.check_balance()


user1 = UserAccount("Jani", 1234, 5000)

user1.welcome()

if user1.authenticate(1234):
    print(f"Hello, {user1.name}!")
    user1.check_balance()
    user1.withdraw(1000)
    user1.deposit(2000)
else:
    print("Authentication failed! Invalid PIN.")


# ============================================================
# Program 6: Child Class with Its Own Method
# ============================================================

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")

    def fetch(self):
        print("Dog is fetching the ball.")


dog = Dog()
dog.sound()
dog.fetch()


# ============================================================
# Program 7: Concrete Method and Instance Method
# ============================================================

class A:

    def show(self):
        pass


obj = A()
obj.show()

print("show() is both a concrete method and an instance method.")
