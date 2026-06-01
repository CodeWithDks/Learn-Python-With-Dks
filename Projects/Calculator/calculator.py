# =========================================================
# WELCOME MESSAGE
# =========================================================

# Print welcome message for calculator

print("Welcome to My Calculator")


# =========================================================
# ADDITION FUNCTION
# =========================================================

def add(num1, num2):
    return num1 + num2


# =========================================================
# SUBTRACTION FUNCTION
# =========================================================

def sub(num1,num2):
    return num1 - num2

# =========================================================
# MULTIPLICATION FUNCTION
# =========================================================

def multi(num1,num2):
    return num1 * num2


# =========================================================
# DIVISION FUNCTION
# =========================================================

def div(num1,num2):

    if num2 !=0:
        return num1 / num2 # return division value
    else:
        return None
    
def power(num1,num2):
    return num1**num2

def modulus(num1,num2):
    if num2 != 0:
        return num1%num2
    else:
        return None

def floor_division(num1,num2):
    if num2 != 0:
        return num1//num2
    else:
        return None
    
def show_menu():
    print("\n" + "="*35)
    print("        SIMPLE CALCULATOR")
    print("="*35)
    print("  Operators:  +   -   *   /   **   %   //")
    print("="*35)

history = []
# =========================================================
# START WHILE LOOP
# =========================================================

while True:
    
    # =====================================================
    # TAKE FIRST NUMBER INPUT
    # =====================================================
    show_menu()

    try:
        num1 = float(input("Enter your first number: "))
    except ValueError:
        print("Invalid number! Please enter a numeric value.")
        continue

    # =====================================================
    # TAKE OPERATOR INPUT
    # =====================================================

    operation = input("Enter your operator (+  -  *  /  **  %  //): ")

    if operation not in ['+', '-', '*', '/','**','%','//']:
        print("Invalid operator! Please use +  -  *  /")
        continue
    # =====================================================
    # TAKE SECOND NUMBER INPUT
    # =====================================================

    try:
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("Invalid number! Please enter a numeric value.")
        continue
    # =====================================================
    # ADDITION CONDITION DEMO
    # =====================================================

    if operation == '+':
        result = add(num1, num2)

    # =====================================================
    # CREATE REMAINING CONDITIONS
    # =====================================================

    elif operation == '-':
        result = sub(num1, num2)
    
    elif operation == '**':
        result = power(num1,num2)
    
    elif operation == '*':
        result = multi(num1, num2)
    
    elif operation == '/':
        result = div(num1, num2)
        if result is None:
            print("Zero is not allowed here")
            continue 

    elif operation == '%':
            result = modulus(num1,num2)
            if result is None:
                print("Zero is not allowed here")
                continue 
   

    elif operation == '//':
        result = floor_division(num1,num2)
        if result is None:
                print("Zero is not allowed here")
                continue      
    
    result = round(result,2)
    print(f"\nResult: {result}")
    history.append(f"{num1} {operation} {num2} = {result}")
    # =====================================================
    # ASK USER TO CONTINUE
    # =====================================================

    while True:
        choice = input("Do you want another calculation? (yes/no): ").lower().strip()
        if choice == "no":
            break
        elif choice == "yes":
            break
        else:
            print("Invalid choice! Please type 'yes' or 'no'.")

    if choice == "no":
          
          break
# =========================================================
# THANK YOU MESSAGE
# =========================================================

# Print thank you message after loop ends

print("\nThanks for using my calculator...")
print("\n" + "="*35)
print("      CALCULATION HISTORY")
print("="*35)
for index, entry in enumerate(history, start=1):
    print(f"  {index}. {entry}")
print("="*35)