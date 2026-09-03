# Encapsulation Programs in Python

# Program 1: Basic Encapsulation - Bank Account

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def show_balance(self):
        print(f"{self.name}, your balance is ₹{self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")


account = BankAccount("Jani", 5000)
account.show_balance()
account.deposit(2000)
account.withdraw(1000)
account.show_balance()


# Program 2: Encapsulation with Account Number Validation

class SecureBankAccount:
    def __init__(self, name, acc_number, balance):
        self.name = name
        self.__acc_number = acc_number
        self.__balance = balance

    def __is_valid_account(self, acc_number):
        return self.__acc_number == acc_number

    def show_balance(self, acc_number):
        if self.__is_valid_account(acc_number):
            print(f"{self.name}, your balance is ₹{self.__balance}")
        else:
            print("Invalid account number.")

    def deposit(self, acc_number, amount):
        if self.__is_valid_account(acc_number):
            if amount > 0:
                self.__balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Invalid account number.")

    def withdraw(self, acc_number, amount):
        if self.__is_valid_account(acc_number):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Invalid account number.")


account = SecureBankAccount("Jani", "ACC123", 5000)

account.show_balance("ACC123")
account.deposit("ACC123", 2000)
account.withdraw("ACC123", 1000)
account.show_balance("ACC123")
account.withdraw("WRONG123", 100)


# Program 3: Simple Getter and Setter Style Methods

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks.")


student = Student("Chahat", 85)

print("Marks:", student.get_marks())

student.set_marks(90)
print("Updated Marks:", student.get_marks())

student.set_marks(120)
