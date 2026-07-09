"""Problem 1 🟢

Create a list of 5 fruits. Print the first, last, and middle item using indexing.
Then add a new fruit to the end and print the full list."""
fruits = ['Apple', 'Mango', 'Orange', 'Papaya', 'Banana']

print(f"First: {fruits[0]}")
print(f"Middle: {fruits[2]}")
print(f"Last: {fruits[-1]}")

fruits.append('Guava')
print(f"Full list: {fruits}")


"""Problem 2 🟡

Ask the user to enter 5 numbers one by one and store them in a list.
Then print the list, the total sum, the highest number, and the lowest number."""

numbers = []
try:
    elements = int(input('How many numbers do you want to store: '))
    i = 1
    while elements >= i:
        try:
            user_input = int(input(f'Enter your {i} number: '))
            numbers.append(user_input)
            i += 1
        except ValueError:
            print('Invalid input, try again')
    
    print('Your numbers:', numbers)
    print('Sum     :', sum(numbers))
    print('Highest :', max(numbers))
    print('Lowest  :', min(numbers))

except ValueError:
    print('Please input a valid number')