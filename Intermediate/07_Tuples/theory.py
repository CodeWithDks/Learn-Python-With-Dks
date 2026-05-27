# Tuple in python.
# A tuple is a collection data type in Python that is ordered and immutable. It is similar to a list, but unlike lists, tuples cannot be modified after they are created. Tuples are defined using parentheses () and can contain elements of different data types. Here are some key features of tuples in Python:

# 1. Ordered: The items in a tuple have a defined order, and that order will not change unless you explicitly modify the tuple (which is not possible since tuples are immutable).
# 2. Immutable: Once a tuple is created, you cannot change its elements. You cannot add, remove, or modify elements in a tuple after it has been created.
# 3. Allow Duplicates: A tuple can contain duplicate items, meaning you can have multiple occurrences of the same value in a tuple.
# 4. Heterogeneous: A tuple can contain items of different data types, such as integers, strings, floats, and even other tuples.
# 5. Indexing and Slicing: You can access individual elements of a tuple using indexing, and you can also access a range of elements using slicing.     




# tuple creation
my_tuple = (1, "Hello", 3.14, (2, 4, 6)) #This is a tuple that contains an integer, a string, a float, and another tuple as its elements.
print(my_tuple) #Output: (1, 'Hello', 3.14, (2, 4, 6))

# How many operations we can perform on tuples.
# Since tuples are immutable, you cannot perform operations that modify the tuple, such as adding or removing elements. However, you can perform various operations on tuples in Python, including:     
# 1. Accessing Elements: You can access individual elements of a tuple using indexing and slicing.
# Example of accessing elements in a tuple  
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])  # Output: 10 (first element)    
print(my_tuple[2])  # Output: 30 (third element)
print(my_tuple[-1])  # Output: 50 (last element)
print(my_tuple[1:4])  # Output: (20, 30, 40) (elements from index 1 to 3)


# 2. Concatenation: You can concatenate two or more tuples using the + operator to create a new tuple.
# Example of tuple concatenation    
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2  # This will create a new tuple (1, 2, 3, 4, 5, 6) by concatenating tuple1 and tuple2.
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6) 


# 3. Repetition: You can repeat a tuple multiple times using the * operator to create a new tuple.
# Example of tuple repetition
tuple = (1, 2, 3)
repeated_tuple = tuple * 3  # This will create a new tuple (1, 2, 3, 1, 2, 3, 1, 2, 3) by repeating the original tuple three times.
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 4. Unpacking: You can unpack the elements of a tuple into individual variables.
# Example of tuple unpacking
my_tuple = (10, 20, 30)
a, b, c = my_tuple  # This will unpack the elements of my_tuple into variables a, b, and c.
print(a)  # Output: 10  
print(b)  # Output: 20
print(c)  # Output: 30


# 5. Built-in Functions: Python provides a variety of built-in functions that can be used with tuples, such as len(), max(), min(), sum(), etc., which allow you to perform various operations on tuples easily.
# Example of built-in functions with tuples
my_tuple = (10, 20, 30)
print(len(my_tuple))  # Output: 3 (number of elements in the tuple)
print(max(my_tuple))  # Output: 30 (maximum value in the tuple)
print(min(my_tuple))  # Output: 10 (minimum value in the tuple)
print(sum(my_tuple))  # Output: 60 (sum of all elements in the tuple)



# Note: Since tuples are immutable, you cannot perform operations that modify the tuple, such as adding or removing elements. If you need a mutable collection, you should use a list instead of a tuple.

# 6. Membership Testing: You can check if an element exists in a tuple using the in keyword.
# Example of membership testing in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True (3 is an element of the tuple)
print(6 in my_tuple)  # Output: False (6 is not an element of the tuple)


# 7. Iteration: You can iterate over the elements of a tuple using a for loop.
# Example of iterating over a tuple
my_tuple = (10, 20, 30)
for element in my_tuple:
    print(element)  # Output: 10, then 20, then 30 (each element printed on a new line) 


# 8. Tuple Methods: Although tuples are immutable, they have a few built-in methods that can be used to perform operations on them, such as count() and index().
# Example of tuple methods
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2 (number of occurrences of 2 in the tuple)
print(my_tuple.index(3))  # Output: 2 (index of the first occurrence of 3 in the tuple)


# 9. Nested Tuples: You can create tuples that contain other tuples as elements, allowing you to create complex data structures.
# Example of nested tuples  
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)  # Output: (1, 2, (3, 4), 5) (a tuple that contains another tuple as one of its elements)


# 10. Tuple Packing: You can create a tuple by packing multiple values together without using parentheses.
# Example of tuple packing  
packed_tuple = 10, 20, 30  # This will create a tuple (10, 20, 30) by packing the values together.
print(packed_tuple)  # Output: (10, 20, 30) (the values are packed into a tuple)


# 11. Tuple Comprehension: Although there is no direct syntax for tuple comprehension, you can create a tuple using a generator expression and the tuple() constructor.
# Example of creating a tuple using a generator expression  
squared_tuple = tuple(x**2 for x in range(5))  # This will create a tuple (0, 1, 4, 9, 16) by generating the squares of numbers from 0 to 4.
print(squared_tuple)  # Output: (0, 1, 4, 9, 16) (a tuple containing the squares of numbers from 0 to 4)


# 12. Tuple Comparison: You can compare tuples using comparison operators like ==, !=, <, >, <=, and >=. The comparison is done element-wise, meaning that the first elements of the tuples are compared first, and if they are equal, the second elements are compared, and so on.
# Example of tuple comparison   
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)  
tuple3 = (1, 2, 4)
print(tuple1 == tuple2)  # Output: True (tuple1 and tuple2 are equal)
print(tuple1 == tuple3)  # Output: False (tuple1 and tuple3 are not equal)
print(tuple1 < tuple3)   # Output: True (tuple1 is less than tuple  3 because the first two elements are equal and the third element of tuple1 is less than the third element of tuple3)    


# 13. Tuple Slicing: You can access a range of elements in a tuple using slicing syntax, similar to how you would slice a list or a string.
# Example of tuple slicing  
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40) (elements from index 1 to 3)
print(my_tuple[:3])   # Output: (10, 20, 30) (elements from the beginning to index 2)
print(my_tuple[3:])   # Output: (40, 50) (elements from index 3 to the end) 


# 14. Tuple Length: You can find the number of elements in a tuple using the len() function.
# Example of finding the length of a tuple  
my_tuple = (10, 20, 30, 40, 50)
print(len(my_tuple))  # Output: 5 (number of elements in the tuple) 


# Where to use tuples in real world applications?
# Tuples are commonly used in real-world applications for various purposes, including:
# 1. Data Integrity: Since tuples are immutable, they are often used to store data that should not be modified after it is created, such as coordinates, RGB color values, or any other fixed set of values.
# 2. Multiple Return Values: Functions can return multiple values as a tuple, allowing you to easily return and unpack multiple pieces of information from a function.
# 3. Dictionary Keys: Tuples can be used as keys in dictionaries because they are immutable, while lists cannot be used as dictionary keys.
# 4. Heterogeneous Data: Tuples can store heterogeneous data, making them useful for representing complex data structures, such as records or database rows, where each element can be of a different type.
# 5. Performance: Tuples can be more memory-efficient than lists, especially when storing a large number of elements, because they are immutable and do not require the overhead of dynamic resizing that lists do. This can make tuples a better choice for certain applications where performance is a concern.   
# 6. Unpacking: Tuples are often used for unpacking values into variables, which can make code more readable and concise when working with multiple values. )
# 7. Function Arguments: Tuples can be used to pass a variable number of arguments to a function using the *args syntax, allowing for flexible function definitions that can handle different numbers of arguments. 
# 8. Named Tuples: The collections module in Python provides a namedtuple class, which allows you to create tuple subclasses with named fields. This can be useful for creating more readable and self-documenting code when working with tuples that represent structured data.    
# 9. Immutable Data Structures: Tuples can be used to create immutable data structures, which can help prevent accidental modification of data and make code more robust and easier to debug.
# 10. Iteration: Tuples can be used in loops and comprehensions to iterate over a fixed set of values, making them useful for scenarios where you need to iterate over a collection of items that should not be modified during the iteration process.  
# 11. Function Arguments and Return Values: Tuples are commonly used to pass multiple arguments to a function or to return multiple values from a function, allowing for more flexible and efficient code when working with functions that need to handle multiple pieces of data.  
# 12. Data Structures: Tuples can be used as building blocks for more complex data structures, such as lists of tuples, dictionaries with tuple keys, or even nested tuples, allowing for the creation of sophisticated data models that can represent a wide variety of real-world scenarios.
# 13. Immutable Collections: Tuples can be used to create immutable collections of data, which can be beneficial in scenarios where you want to ensure that the data cannot be modified after it is created, such as in multi-threaded applications or when working with shared data across different parts of a program.
# 14. Performance Optimization: In some cases, using tuples instead of lists can lead to performance improvements, especially when working with large datasets or when the data is not expected to change, as tuples can be more memory-efficient and faster to access than lists due to their immutability.
# 15. Data Analysis and Machine Learning: Tuples are often used in data analysis and machine learning applications to represent fixed sets of data, such as feature vectors, labels, or coordinates, where the immutability of tuples can help ensure the integrity of the data throughout the analysis process.
# 16. Configuration and Constants: Tuples can be used to store configuration settings or constants in a program, providing a convenient way to group related values together while ensuring that they cannot be modified accidentally during the execution of the program.
# 17. API Design: When designing APIs, tuples can be used to return multiple values from a function or to represent structured data in a way that is easy for users of the API to understand and work with, while also ensuring that the data remains immutable and consistent throughout the API's usage.  
# 18. Data Serialization: Tuples can be used in data serialization formats, such as JSON or XML, to represent fixed sets of data that need to be transmitted or stored in a structured format, allowing for efficient and organized data representation in various applications.
# 19. Graphical User Interfaces: In GUI programming, tuples can be used to represent coordinates, dimensions, or other fixed sets of values that are needed to define the layout and behavior of graphical elements, providing a convenient way to manage and manipulate these values in a structured manner.
# 20. Scientific Computing: In scientific computing and numerical analysis, tuples can be used to represent fixed sets of parameters, such as the dimensions of a matrix, the coefficients of a polynomial, or the parameters of a mathematical model, allowing for efficient and organized representation of these values in computational applications.
#    




# Differences between lists and tuples in table format:
# | Feature           | List                          | Tuple                         |
# |-------------------|-------------------------------|-------------------------------| 
# | Mutability        | Mutable (can be modified)     | Immutable (cannot be modified) |
# | Syntax            | Defined using square brackets [] | Defined using parentheses () |
# | Performance       | Generally slower than tuples   | Generally faster than lists    |
# | Use Cases         | Suitable for collections of items that may need to be modified, such as lists of data, dynamic collections, etc. | Suitable for fixed collections of items that should not be modified, such as coordinates, RGB values, etc. | 






