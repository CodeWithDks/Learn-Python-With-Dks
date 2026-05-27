# Condional in Python
# 1. If Statement: The if statement is used to execute a block of code only if a specified condition is true.

# Example of If Statement
age = 18
if age >= 18:
    print("You are an adult.") #This code will be executed because the condition (age >= 18) is true.


# 2. If-Else Statement: The if-else statement is used to execute one block of code if a specified condition is true, and another block of code if the condition is false. 

# Example of If-Else Statement
age = 16
if age >= 18:
    print("You are an adult.") #This code will not be executed because the condition (age >= 18) is false.  
else:
    print("You are a minor.") #This code will be executed because the condition (age >= 18) is false.

# 3. Elif Statement: The elif statement is used to check multiple conditions. It stands for "else if" and allows you to specify additional conditions to check if the previous conditions were false.   
# 
# Example of Elif Statement
age = 65
if age < 18:    
    print("You are a minor.") #This code will not be executed because the condition (age < 18) is false.
elif age >= 18 and age < 65:
    print("You are an adult.") #This code will not be executed because the condition (age >= 18 and age < 65) is false. 
else:
    print("You are a senior citizen.") #This code will be executed because the previous conditions were false, and the else block is executed when all previous conditions are false.

# 4. Nested If Statements: You can also have if statements inside other if statements, which are called nested if statements. This allows you to check for multiple conditions in a more complex way.

# Example of Nested If Statements
age = 20
if age >= 18:   
    if age < 21:
        print("You are an adult but not old enough to drink alcohol in the US.") #This code will be executed because the condition (age >= 18) is true, and the nested condition (age < 21) is also true.
    else:
        print("You are an adult and old enough to drink alcohol in the US.") #This code will not be executed because the nested condition (age < 21) is false.  
else:
    print("You are a minor.") #This code will not be executed because the condition (age >= 18) is true, and the else block is executed when the condition is false.



