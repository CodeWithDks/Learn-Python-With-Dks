'''
Theme: while loops
Problem 1 🟢

Keep asking the user to enter a positive number until they actually do. Once they enter a valid positive number,
print "Thank you! You entered: [number]".

'''

while True:
    try:
        user_input = int(input("Enter a number: "))

        if user_input > 0:
            print(f"Thank you! You entered:{user_input}")
            break
        else:
            print("Please enter a positive number")
            continue

    except ValueError:
        print("Invalid input.")



'''
Problem 2 🟡

Write a program that counts down from a number the user enters, printing each number, then prints "Blast off!"
when it hits 0. If the user enters a negative number, print "Please enter a positive number" and ask again.

'''

while True:

    try:
        number = int(input('Enter a number: '))

        if number < 0:
            print("please enter a positive number")
            continue
        else:
            while number >= 0:
                print(number)
                number -= 1
            print('Blast off!')
            break
    except ValueError:
        print('Invalid input.')
