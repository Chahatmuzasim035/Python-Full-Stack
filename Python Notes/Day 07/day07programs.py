# DAY 7 - PYTHON STRINGS
# 1. Creating strings
single_quote = 'Hello'
double_quote = "Python"
multi_line = """This is
a multi-line string."""

print(single_quote)
print(double_quote)
print(multi_line)


# 2. Concatenation
first = "Hello"
second = "World"
print(first + " " + second)


# 3. Repetition
print("Python! " * 3)


# 4. Indexing
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])


# 5. Slicing
print("First three:", text[0:3])
print("First four:", text[:4])
print("From index 2:", text[2:])


# 6. Membership
print("Py" in text)
print("Java" not in text)


# 7. Built-in functions
sample = "Hello World"
print("Length:", len(sample))
print("Maximum:", max("abcXYZ"))
print("Minimum:", min("abcXYZ"))
print("Sorted:", sorted("python"))
print("Code of A:", ord("A"))
print("Character 97:", chr(97))
# 8. Case conversion
word = "PyThOn programming"

print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.title())
print(word.swapcase())
print("STRAẞE".casefold())
# 9. Alignment and formatting
print("python".center(12, "*"))
print("py".ljust(6, "-"))
print("py".rjust(6, "-"))
print("42".zfill(5))
# 10. Searching
sentence = "banana"

print("First a:", sentence.find("a"))
print("Last a:", sentence.rfind("a"))
print("First a with index:", sentence.index("a"))
print("Last a with rindex:", sentence.rindex("a"))
print("Number of a:", sentence.count("a"))
# 11. String tests
value = "Hello"

print("Starts with He:", value.startswith("He"))
print("Ends with lo:", value.endswith("lo"))
print("Only alphabets:", value.isalpha())
print("Alphanumeric:", "abc123".isalnum())
print("Lowercase:", value.islower())
print("Uppercase:", "HELLO".isupper())
print("Whitespace:", "   ".isspace())
print("Title case:", "Hello World".istitle())
print("Valid identifier:", "variable1".isidentifier())


# 12. Decimal, digit and numeric checks
print("123 is decimal:", "123".isdecimal())
print("² is digit:", "²".isdigit())
print("⅓ is numeric:", "⅓".isnumeric())


# 13. Replace
fruit = "apple"
print(fruit.replace("p", "b"))


# 14. Translation
table = str.maketrans("abc", "xyz")
print("abc".translate(table))


# 15. Split
csv_data = "red,green,blue"
print(csv_data.split(","))


# 16. Right split
data = "one,two,three"
print(data.rsplit(",", 1))


# 17. Split lines
lines = "Hello\nPython"
print(lines.splitlines())


# 18. Join
parts = ["Hello", "Python"]
print(" ".join(parts))


# 19. Partition
print("apple-pie".partition("-"))
print("apple-pie".rpartition("-"))


# 20. Strip, lstrip and rstrip
print("  hello  ".strip())
print("---hello".lstrip("-"))
print("hello---".rstrip("-"))


# 21. Encoding
message = "Hello Python"
encoded = message.encode("utf-8")
print("Encoded:", encoded)


# 22. Decoding
decoded = encoded.decode("utf-8")
print("Decoded:", decoded)


# 23. Mini practice: count a character
text = "banana"
character = "a"
print("Occurrences:", text.count(character))


# 24. Mini practice: reverse using slicing
word = "Python"
print("Reversed:", word[::-1])


# 25. Mini practice: clean and format text
raw_name = "   chahat muzAsim   "
clean_name = raw_name.strip().title()
print("Formatted name:", clean_name)