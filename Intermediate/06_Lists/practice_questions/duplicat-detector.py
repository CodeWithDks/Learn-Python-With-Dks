'''Duplicate Detector

Take list:

[1, 2, 3, 2, 5, 1]

Find duplicate elements.

Skills
loops
comparison logic
collection thinking'''

# Taking user input for the list
input_list = input("Enter a list of numbers separated by commas: ")

# Converting the input string into a list of integers
numbers = [int(num.strip()) for num in input_list.split(",")]

# Finding duplicate elements
duplicates = set()
unique_numbers = set()  
for num in numbers:
    if num in unique_numbers:
        duplicates.add(num)
    else:
        unique_numbers.add(num)

# Printing the duplicate elements
if duplicates:
    print("Duplicate elements:", duplicates)
else:
    print("No duplicate elements found.")