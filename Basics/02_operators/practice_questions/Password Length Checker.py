# Password Length Checker


# Taking input from user.
password = input("Please enter your password: ")


# Checking the length of the password and providing feedback to the user.
if len(password) >= 8:
    print("You have entered strong password")
    print(f"You used {len(password)} character in your password.")
else:
    print("Please enter your password more than 8 characters.")