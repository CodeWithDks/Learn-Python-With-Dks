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

