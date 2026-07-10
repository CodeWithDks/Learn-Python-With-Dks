import random

while True:
    # Ask the user for play permission
    roll = input('Roll the dice? (yes/no): ')

    # checking condition
    if roll == 'yes':
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(f'Your dice numers is: ({num1},{num2})')

    elif roll == 'no':
        print('Thanks for playing......')
        break

    else:
        print('Invalid input')