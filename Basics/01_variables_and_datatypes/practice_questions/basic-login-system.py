#basic-login-system# Create a simple login system that checks if the username and password entered by the user match a predefined username and password. If they match, print "Login successful!", otherwise print "Login failed!".


# Predefined username & password.
predefined_username ='Radha'
predefined_password ='password123'


# Taking user inputs
username = input("Enter username: ")
password = input("Enter password: ")


# Cheching username & password matching or not.
if username==predefined_username and password==predefined_password:
    print('Login successfully')
elif username != predefined_username and password==predefined_password:
    print("inviald username")
elif username == predefined_username and password!=predefined_password:
    print("inviald passowrd")
else:
    print("invaild inputs..")