"""
Print the multiplication table for a number the user enters. Format it like:

3 x 1 = 3
3 x 2 = 6
... up to 10.

"""
try:

    number = int(input("Enter the number for table: "))

    if number > 0:
        print(f'The table of {number}:')
        for i in range(1,11):
            print(f"{number} * {i} = {number*i}")

    else:
        print("Please enter a positive number.")
except ValueError:
    print("Invalid Input!")
'''
Problem 2 🟡

Ask the user for a number n. Print the sum of all numbers from 1 to n. 
Then also print which numbers in that range are even and which are odd, each on a separate labeled line.
Example: "Even: 2", "Odd: 3"
'''
try:
    num = int(input("Enter a number: "))
    total = 0
    for i in range(1, num + 1):
        total += i
        if i % 2 == 0:
            print(f"Even: {i}")
        else:
            print(f"Odd: {i}")
    print(f"Sum of 1 to {num}: {total}")
except ValueError:
    print("Invalid input!")