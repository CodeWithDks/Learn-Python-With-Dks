"""
Question 1 — Character Extractor

Take a user name.

Print:

first character
last character
Example

Input:

Deepak

Output:

First character: D
Last character: k
"""

# Taking user input for the name
name = input("Enter your name: ")

# Extracting the first and last characters
first_character = name[0]
last_character = name[-1]

# Printing the results
print(f"First character: {first_character}")
print(f"Last character: {last_character}")
