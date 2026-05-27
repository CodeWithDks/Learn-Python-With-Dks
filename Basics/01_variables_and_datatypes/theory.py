# VARIABLES AND DATA TYPES IN PYTHON!
# A variable is a container for storing data values. In Python, you don't need to declare the type of a variable; it is determined automatically based on the value assigned to it.  


1.# What is a variable in Python?
# A variable in Python is a named location in memory that is used to store data. It can hold different types of data, such as numbers, strings, lists, etc. Variables are created when you assign a value to them, and they can be used to manipulate and access the stored data throughout the program.

2.# What is dynamic typing in Python?
# Dynamic typing in Python means that the type of a variable is determined at runtime, and it can change as the program executes. This allows you to assign different types of values to the same variable without causing an error. For example, you can assign an integer to a variable and later assign a string to the same variable without any issues.
x = 10  # x is an integer
print(x)  # Output: 10
x = "Hello"  # x is now a string
print(x)  # Output: Hello

3. # What is the difference between int, float, and str?
# int (integer) is a data type that represents whole numbers without a decimal point. For example, 5, -3, and 0 are all integers.
# float (floating-point) is a data type that represents numbers with a decimal point. For example, 3.14, -0.5, and 0.0 are all floats.
# str (string) is a data type that represents a sequence of characters. It is used to store text. For example, "Hello", 'Python', and "123" are all strings. Strings can be enclosed in either single quotes (' ') or double quotes (" ").

4. # Is Python strongly typed or weakly typed? Explain briefly.
# Python is a strongly typed language, which means that it does not allow implicit type conversion between different data types. If you try to perform an operation on incompatible types, Python will raise a TypeError. For example, if you try to add an integer and a string, Python will not automatically convert the integer to a string or vice versa; instead, it will raise an error. This helps prevent unintended behavior and makes the code more predictable.
x = 5
y = "10"
# This will raise a TypeError because you cannot add an integer and a string directly.
# result = x + y  # Uncommenting this line will cause an error.

5.# What is type conversion? Why is it important?
# Type conversion, also known as type casting, is the process of converting a value from one data type to another. It is important because it allows you to perform operations on different types of data and ensures that the data is in the correct format for the intended operation. For example, if you want to add two numbers that are stored as strings, you need to convert them to integers or floats first. Type conversion can be done using built-in functions like int(), float(), and str().
# Example of type conversion
num_str = "10"
num_int = int(num_str)  # Convert string to integer
print(num_int)  # Output: 10
num_float = float(num_str)  # Convert string to float
print(num_float)  # Output: 10.0

6.# What is the difference between:
    
int(5.9) and float(5)
# int(5.9) will convert the floating-point number 5.9 to an integer by truncating the decimal part, resulting in 5. On the other hand, float(5) will convert the integer 5 to a floating-point number, resulting in 5.0. The int() function removes the decimal part and returns an integer, while the float() function adds a decimal point and returns a floating-point number.
print(int(5.9))  # Output: 5
print(float(5))  # Output: 5.0

   
7. # What happens if you try to add an int and a str?
# If you try to add an int and a str, Python will raise a TypeError because it does not allow implicit type conversion between these two types. You cannot directly add a number and a string together without converting one of them to the other type first. For example, if you try to execute the following code:
x = 5
y = "10"
result = x + y  # This will raise a TypeError
# To avoid this error, you can convert the integer to a string or the string to an integer before performing the addition. For example:
# Convert integer to string
result = str(x) + y  # This will concatenate the string "5" and "10", resulting in "510"
print(result)  # Output: "510"
# Convert string to integer
result = x + int(y)  # This will add the integer 5 and the integer 10, resulting in 15
print(result)  # Output: 15

8. # What is the difference between:
   # "5" and 5
   # "5" is a string, which is a sequence of characters enclosed in quotes. It represents the character '5' as text. On the other hand, 5 is an integer, which is a numeric data type that represents the whole number 5. The string "5" cannot be used in mathematical operations without converting it to an integer, while the integer 5 can be used directly in calculations. For example:
print("5" + "5")  # Output: "55" (string concatenation)
print(5 + 5)    # Output: 10 (integer addition)     

9. # Can a variable change its data type after assignment? Explain with example.
# Yes, a variable in Python can change its data type after assignment due to Python's dynamic typing. This means that you can assign a value of one type to a variable and later assign a value of a different type to the same variable without any issues. For example:
x = 10  # x is an integer
print(x)  # Output: 10
x = "Hello"  # x is now a string
print(x)  # Output: Hello
x = 3.14  # x is now a float
print(x)  # Output: 3.14


10. # What is the difference between:
    
x = 10
    
x = "10"
# In the first case, x is assigned the integer value 10, which is a numeric data type. In the second case, x is assigned the string value "10", which is a sequence of characters. The variable x can hold different types of data due to Python's dynamic typing, and it can change its type based on the value assigned to it. The integer 10 can be used in mathematical operations, while the string "10" cannot be used in calculations without converting it to an integer first.
