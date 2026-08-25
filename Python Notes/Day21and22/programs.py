# ==========================================
# PYTHON OOP – DAY 22 & DAY 23
# ==========================================


# 1. Creating a Class

class Product:
    pass


# 2. Creating Objects

laptop = Product()
mobile = Product()
headphones = Product()

print(laptop)
print(mobile)
print(headphones)


# 3. Class Attribute

class Product:
    platform = "Flipkart"


laptop = Product()
mobile = Product()

print(Product.platform)
print(laptop.platform)
print(mobile.platform)


# 4. Creating Multiple Objects

class Product:
    platform = "Flipkart"


product1 = Product()
product2 = Product()
product3 = Product()
product4 = Product()
product5 = Product()

print(product1.platform)
print(product2.platform)
print(product3.platform)


# 5. Instance Attributes

class Product:
    platform = "Flipkart"

    def set_product(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand


laptop = Product()
mobile = Product()

laptop.set_product("HP Laptop", 55000, "HP")
mobile.set_product("Samsung Galaxy", 28000, "Samsung")

print(laptop.name)
print(laptop.price)
print(laptop.brand)

print(mobile.name)
print(mobile.price)
print(mobile.brand)


# 6. Instance Method

class Product:

    def display_product(self):
        print("Displaying Product Details")

    def check_stock(self):
        print("Stock Available")


laptop = Product()

laptop.display_product()
laptop.check_stock()


# 7. Class Method

class Product:
    delivery_charge = 40

    @classmethod
    def update_delivery_charge(cls):
        cls.delivery_charge = 60


print(Product.delivery_charge)

Product.update_delivery_charge()

print(Product.delivery_charge)


# 8. Static Method

class Product:

    @staticmethod
    def free_delivery(price):
        return price >= 500


print(Product.free_delivery(800))
print(Product.free_delivery(300))


# 9. Accessing Class Attribute Using Object

class Product:
    platform = "Flipkart"


laptop = Product()

print(laptop.platform)


# 10. Accessing Class Attribute Using Class Name

class Product:
    platform = "Flipkart"


print(Product.platform)


# 11. Accessing Instance Method

class Product:

    def display_product(self):
        print("Displaying Product Details")


laptop = Product()

laptop.display_product()


# 12. Accessing Class Method

class Product:
    delivery_charge = 40

    @classmethod
    def show_delivery_charge(cls):
        print(cls.delivery_charge)


Product.show_delivery_charge()

product = Product()
product.show_delivery_charge()


# 13. Accessing Static Method

class Product:

    @staticmethod
    def free_delivery(price):
        return price >= 500


print(Product.free_delivery(700))

product = Product()

print(product.free_delivery(300))


# 14. Complete OOP Example

class Product:

    platform = "Flipkart"

    def display_product(self):
        print("Welcome to Flipkart")

    @classmethod
    def show_platform(cls):
        print(cls.platform)

    @staticmethod
    def free_delivery(price):
        return price >= 500


laptop = Product()

print(laptop.platform)

laptop.display_product()

Product.show_platform()

print(Product.free_delivery(700))