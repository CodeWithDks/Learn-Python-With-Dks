# =========================================================
# WELCOME MESSAGE
# =========================================================

# Print welcome message for calculator

print("Welcome to My Calculator")


# =========================================================
# ADDITION FUNCTION
# =========================================================

# Create function name: add
# Take two parameters
# Return addition value

def add(num1, num2):
    return num1 + num2


# =========================================================
# SUBTRACTION FUNCTION
# =========================================================

# Create function name: sub
# Take two parameters
# Return subtraction value

def sub(num1,num2):
    return num1 - num2

# =========================================================
# MULTIPLICATION FUNCTION
# =========================================================

# Create function name: multi
# Take two parameters
# Return multiplication value

def multi(num1,num2):
    return num1 * num2


# =========================================================
# DIVISION FUNCTION
# =========================================================

# Create function name: div
# Take two parameters

def div(num1,num2):

# Check:
# if second number is not zero
    if num2 !=0:
        return num1 / num2 # return division value
    else:
        return "You can't divide with zero." # returned error message


# =========================================================
# START WHILE LOOP
# =========================================================

# Create infinite loop

while True:
    
    # =====================================================
    # TAKE FIRST NUMBER INPUT
    # =====================================================

    # Take first number from user
    # Convert into float
    # Store inside variable:
    # num1
    num1 = float(input("Enter your first number: "))
    


    # =====================================================
    # TAKE OPERATOR INPUT
    # =====================================================

    # Ask user for operator
    #
    # Example:
    # +  -  *  /
    #
    # Store inside variable:
    # operation

    operation = input("Enter your operator (+  -  *  /): ")


    # =====================================================
    # TAKE SECOND NUMBER INPUT
    # =====================================================

    # Take second number from user
    # Convert into float
    # Store inside variable:
    # num2

    num2 = float(input("Enter your second number: "))


    # =====================================================
    # ADDITION CONDITION DEMO
    # =====================================================

    # Check:
    # if operation is '+'
    #
    # Call add function
    # Store returned value inside variable:
    # result
    #
    # Print result

    if operation == '+':
        result = add(num1, num2)
        print("Result:", result)


    # =====================================================
    # CREATE REMAINING CONDITIONS
    # =====================================================

    elif operation == '-':
        result = sub(num1, num2)
        print("Result:", result)
    
    elif operation == '*':
        result = multi(num1, num2)
        print("Result:", result)
    
    elif operation == '/':
        result = div(num1, num2)
        print("Result:", result)
    
    else:
        print("Invalid input")

    # =====================================================
    # ASK USER TO CONTINUE
    # =====================================================

    # Ask user:
    # "Do you want another calculation?"
    #
    # Store answer inside variable:
    # choice

    choice = input("Do you want another calculation (yes/no)?: ").lower().strip()


    # =====================================================
    # STOP THE LOOP
    # =====================================================

    # Check:
    # if choice == "no"
    if choice == "no":
        break


# =========================================================
# THANK YOU MESSAGE
# =========================================================

# Print thank you message after loop ends

print("Thanks for using my calculator...")