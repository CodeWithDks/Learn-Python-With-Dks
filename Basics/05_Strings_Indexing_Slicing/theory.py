# String in python

# A string is a sequence of characters enclosed in quotes. In Python, you can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) to create a string.

# Example of a string
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!

# String Indexing: Each character in a string has an index, starting from 0 for the first character. You can access individual characters in a string using their index.

# Example of string indexing
my_string = "Hello, World!"
print(my_string[0])  # Output: H
print(my_string[7])  # Output: W  


# what is indexing in python?
# Indexing in Python refers to the process of accessing individual elements of a sequence (like a string, list, or tuple) using their position or index. In Python, indexing starts at 0, which means the first element of a sequence is accessed with index 0, the second element with index 1, and so on. You can use square brackets [] to access elements by their index. For example, if you have a string "Hello", you can access the first character 'H' using my_string[0], the second character 'e' using my_string[1], and so on. Negative indexing is also supported, where -1 refers to the last element, -2 to the second last, and so forth.
my_string = "Hello"
print(my_string[0])  # Output: H (first character)
print(my_string[1])  # Output: e (second character)
print(my_string[-1])  # Output: o (last character)


# What is slicing in python?
# Slicing in Python is a technique used to access a range of elements in a sequence (like a string, list, or tuple) by specifying a start and end index. The syntax for slicing is sequence[start:end], where start is the index of the first element you want to include, and end is the index of the first element you want to exclude. Slicing allows you to create a new sequence that contains only the specified range of elements. You can also omit the start or end index to slice from the beginning or to the end of the sequence, respectively.
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello (characters from index 0 to 4)
print(my_string[7:12])  # Output: World (characters from index 7 to 11)
print(my_string[:5])  # Output: Hello (same as my_string[0: 5])
print(my_string[7:])  # Output: World! (same as my_string[7:len(my_string)])    



# Why indexing is negative in python?
# Negative indexing in Python allows you to access elements from the end of a sequence (like a string, list, or tuple) instead of the beginning. The last element of the sequence is accessed with index -1, the second last with index -2, and so on. This feature is useful when you want to access elements relative to the end of the sequence without needing to know its length. For example, if you have a string "Hello", you can access the last character 'o' using my_string[-1], the second last character 'l' using my_string[-2], and so on. Negative indexing provides a convenient way to work with sequences when you are interested in elements near the end.
my_string = "Hello"
print(my_string[-1])  # Output: o (last character)
print(my_string[-2])  # Output: l (second last character)



# String Slicing: You can also access a range of characters in a string using slicing. The syntax for slicing is string[start:end], where start is the index of the first character you want to include, and end is the index of the first character you want to exclude.

# Example of string slicing
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
print(my_string[7:12])  # Output: World

# You can also omit the start or end index in slicing. If you omit the start index, it defaults to 0. If you omit the end index, it defaults to the length of the string.

# Example of slicing with omitted indices
my_string = "Hello, World!"
print(my_string[:5])  # Output: Hello (same as my_string[0:5])
print(my_string[7:])  # Output: World! (same as my_string[7:len(my_string)])

# How many operations we can perform on strings.
# We can perform various operations on strings in Python, including:
# 1. Concatenation: Combining two or more strings using the + operator.
# Example of concatenation
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)  # Output: Hello World

# 2. Repetition: Repeating a string multiple times using the * operator. 
# Example of repetition
string = "Hello"
print(string * 3)  # Output: HelloHelloHello

# 3. Slicing: Extracting a portion of a string using slicing syntax.
# Example of slicing
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello (characters from index 0 to 4)
print(my_string[7:12])  # Output: World (characters from index 7 to 11)

# 4. Indexing: Accessing individual characters in a string using their index.
# Example of indexing
my_string = "Hello, World!" 
print(my_string[0])  # Output: H (first character)
print(my_string[7])  # Output: W (eighth character)

# 5. Length: Finding the length of a string using the len() function.
# Example of length
my_string = "Hello, World!"
print(len(my_string))  # Output: 13 (number of characters in the string)

# 6. Case Conversion: Changing the case of characters in a string using methods like upper(), lower(), title(), etc.
# Example of case conversion
my_string = "Hello, World!"
print(my_string.upper())  # Output: HELLO, WORLD! (converts all characters to uppercase)
print(my_string.lower())  # Output: hello, world! (converts all characters to lowercase)
print(my_string.title())  # Output: Hello, World! (converts the first character of each word to uppercase)

# 7. Stripping: Removing whitespace from the beginning and end of a string using the strip() method.
# Example of stripping
my_string = "   Hello, World!   "
print(my_string.strip())  # Output: Hello, World! (removes leading and trailing whitespace)

# 8. Splitting: Breaking a string into a list of substrings using the split() method.
# Example of splitting
my_string = "Hello, World!"
print(my_string.split(","))  # Output: ['Hello', ' World!']

# 9. Joining: Combining a list of strings into a single string using the join() method.
# Example of joining
my_list = ["Hello", "World"]
print(", ".join(my_list))  # Output: Hello, World

# 10. Replacing: Replacing occurrences of a substring with another substring using the replace() method.
# Example of replacing
my_string = "Hello, World!"
print(my_string.replace("World", "Python"))  # Output: Hello, Python! (replaces "World" with "Python")

# 11. Finding: Searching for a substring within a string using the find() method.
# Example of finding
my_string = "Hello, World!"
print(my_string.find("World"))  # Output: 7 (returns the index of the first occurrence of "World")


# 12. Formatting: Inserting values into a string using format() method or f-strings.
# Example of formatting
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Using format() method
print(f"My name is {name} and I am {age} years old.")  # Using f-strings (available in Python 3.6 and later)

# 13. Checking for Substring: Using the in keyword to check if a substring exists
# Example of checking for substring
my_string = "Hello, World!"
print("World" in my_string)  # Output: True (checks if "World" is a substring of my_string)
print("Python" in my_string)  # Output: False (checks if "Python" is a substring of my_string)

# 14. Escaping Characters: Using backslashes to include special characters in a string.
# Example of escaping characters
my_string = "He said, \"Hello, World!\""
print(my_string)  # Output: He said, "Hello, World!" (the backslashes allow us to include double quotes in the string)

# 15. String Methods: Python provides a wide range of built-in string methods for various operations, such as isalpha(), isdigit(), startswith(), endswith(), etc.  
# Example of string methods
my_string = "Hello123"
print(my_string.isalpha())  # Output: False (checks if all characters are alphabetic)
print(my_string.isdigit())  # Output: False (checks if all characters are digits)   
print(my_string.startswith("Hello"))  # Output: True (checks if the string starts with "Hello")
print(my_string.endswith("123"))  # Output: True (checks if the string ends with "123")
    





