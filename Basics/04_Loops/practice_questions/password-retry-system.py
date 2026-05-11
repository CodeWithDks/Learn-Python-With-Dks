# Password Retry System

# set a password
password = 'secret123'
counter = 0
max_attempts = 3
while counter < max_attempts:
    # ask user to enter password
    user_input = input("Enter the password: ")
    counter += 1
    # check if the entered password is correct
    if user_input == password:
        print("Access granted!")
        break  # exit the loop if the password is correct
    elif counter < max_attempts:
        print(f"Incorrect password. You have {max_attempts - counter} attempts left.")
    else:
        print("Incorrect password. Please try again.")