# VARIABLES AND DATA TYPES IN PYTHON!
# A variable is a container for storing data values. In Python, you don't need to declare the type of a variable; it is determined automatically based on the value assigned to it.
# Here are some examples of variables and their data types in Python:

# String: A sequence of characters enclosed in quotes.
name = "Radha"

# Integer: A whole number without a decimal point.
age = 25


# Float: A number with a decimal point.
height = 5.6

# Boolean: A value that can be either True or False.
is_student = True

# List: An ordered collection of items, which can be of different types.
fruits = ["apple", "banana", "cherry"]

# Tuple: An ordered, immutable collection of items.
coordinates = (10.0, 20.0)

# Dictionary: A collection of key-value pairs.
person = {"name": "Radha", "age": 25, "height": 5.6}

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# You can also use the type() function to check the data type of a variable.
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>
print(type(fruits))  # Output: <class 'list'>
print(type(coordinates))  # Output: <class 'tuple'>
print(type(person))  # Output: <class 'dict'>   

