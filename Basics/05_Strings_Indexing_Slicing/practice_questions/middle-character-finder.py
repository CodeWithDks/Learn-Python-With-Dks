"""
Middle Character Finder

Take a word.

Print:

middle character

Example:

Python

Output: t

"""
# Taking user input for the word
word = input("Enter a word: ").strip()  # Removing any leading/trailing whitespace

# Finding the middle character
length = len(word)

if length % 2 == 1:  # If the length of the word is odd
    middle_index = length // 2
    middle_character = word[middle_index]
    print(f"Middle character: {middle_character}")
else:  # If the length of the word is even
    middle_index1 = (length // 2) - 1
    middle_index2 = length // 2
    middle_characters = word[middle_index1] + word[middle_index2]
    print(f"Middle characters: {middle_characters}")

