"""Problem 1 🟡

Write a number guessing game. The program picks a random number between 1 and 50 (use import random). 
The user keeps guessing until they get it right. 
After each wrong guess, tell them "Too high" or "Too low". 
Count and print the number of attempts it took when they win."""


# solution:

import random

target = random.randint(1, 50)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    try:
        guess = int(input("Guess the number (1-50): "))

        if not 1 <= guess <= 50:
            print("Please enter a number between 1 and 50.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == target:
            print(f"You guessed it correctly in {attempts} attempt(s)! The number was {target}.")
            break
        elif guess > target:
            print(f"Too high! Attempts left: {remaining}")
        else:
            print(f"Too low! Attempts left: {remaining}")

    except ValueError:
        print("Invalid input! Please enter an integer.")

else:
    print(f"You've used all {max_attempts} attempts. The correct number was {target}.")




"""Problem 2 🟠

Write a program that prints the first n prime numbers, where n is given by the user.
(Hint: a prime number is only divisible by 1 and itself — you'll need a nested loop to check divisibility.)"""

# solution: 

while True:
    try:
        n = int(input("Enter how many prime numbers you want: "))

        if n <= 0:
            print("Please enter a positive integer.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

count = 0
num = 2

while count < n:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1

print(f"\nTotal prime numbers = {count}")