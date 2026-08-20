# DAY 18 - LIST COMPREHENSION & GENERATORS

# 1. Squares
squares = [x * x for x in range(6)]
print(squares)


# 2. Even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)


# 3. Uppercase names
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)


# 4. Uppercase product names
products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [product.upper() for product in products]
print(upper_products)


# 5. Apply 10% discount
prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
print(discounted)


# 6. Indexes of products in stock
in_stock = [True, False, True, False]
available = [i for i, stock in enumerate(in_stock) if stock]
print(available)


# 7. Products costing more than 700
product_info = [
    ("Laptop", 1000),
    ("Phone", 800),
    ("Tablet", 450)
]

expensive = [name for name, price in product_info if price > 700]
print(expensive)


# 8. Available product names
products_data = [
    {"name": "Laptop", "price": 1000, "stock": 3},
    {"name": "Phone", "price": 800, "stock": 0},
    {"name": "Tablet", "price": 450, "stock": 5}
]

available_names = [
    product["name"]
    for product in products_data
    if product["stock"] > 0
]

print(available_names)


# 9. Discounted prices for available products
discounted_products = [
    {product["name"]: product["price"] * 0.9}
    for product in products_data
    if product["stock"] > 0
]

print(discounted_products)


# 10. Add 100 to each price
prices = [200, 400, 600]
new_prices = [price + 100 for price in prices]
print(new_prices)


# 11. Round float values
prices = [99.99, 120.456, 45.678]
rounded_prices = [round(price * 1.1, 2) for price in prices]
print(rounded_prices)


# 12. Nested list comprehension
products_colors = [
    {"name": "Laptop", "colors": ["Silver", "Black"]},
    {"name": "Phone", "colors": ["Gold", "Blue"]}
]

all_colors = [
    color
    for product in products_colors
    for color in product["colors"]
]

print(all_colors)


# 13. Available products with discounted prices
result = [
    f"{product['name']} - ${product['price'] * 0.9:.2f}"
    for product in products_data
    if product["stock"] > 0
]

print(result)


# 14. Simple generator
def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))


# 15. Count up to a limit
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))


# 16. Generator with for loop
for value in count_up_to(5):
    print(value)


# 17. Square number generator
def square_numbers(n):
    for i in range(n):
        yield i * i


squares = square_numbers(5)
print(next(squares))
print(next(squares))
print(next(squares))


# 18. Print generated squares
for value in square_numbers(6):
    print(value)


# 19. Countdown generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


cd = countdown(5)
print(next(cd))
print(next(cd))
print(next(cd))


# 20. Countdown with for loop
for value in countdown(5):
    print(value)


# 21. Even number generator
def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


for value in even_numbers(10):
    print(value)


# 22. Multiplication table generator
def multiplication_table(number):
    for i in range(1, 11):
        yield number * i


for value in multiplication_table(5):
    print(value)


# 23. Name generator
def name_generator(names):
    for name in names:
        yield name


name_values = name_generator(["Alice", "Bob", "Charlie"])
print(next(name_values))
print(next(name_values))


# 24. Data chunk generator
def stream_data(data):
    for item in data:
        yield item


stream = stream_data(["Chunk 1", "Chunk 2", "Chunk 3"])
print(next(stream))
print(next(stream))
print(next(stream))