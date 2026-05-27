# Operators in python are special symbols that perform specific operations on one or more operands. They are used to manipulate data and variables in various ways. Here are some common types of operators in Python:

# 1. Arithmetic Operators: These operators perform basic mathematical operations.

# Example of Arithmetic Operators

a = 10
b = 5

print("Addition:", a+b) #Addition (+) is used to add two numbers together. For example, 10+5 will give you 15, because when you add 10 and 5 together, the result is 15.

print("Subtraction:", a-b) #Subtraction (-) is used to find the difference between two numbers. For example, 10-5 will give you 5, because when you subtract 5 from 10, the result is 5.

print("Multiplication:", a*b) #Multiplication (*) is used to find the product of two numbers. For example, 10*5 will give you 50, because when you multiply 10 by 5, the result is 50.

print("Division:", a/b) #Division (/) returns a floating-point result, even if both operands are integers. For example, 10/5 will give you 2.0, not 2, because the division operator always returns a float in Python.

print("Floor Division:", a//b) #Floor Division (//) returns the largest integer less than or equal to the division of the two numbers. For example, 10//3 will give you 3, because when you divide 10 by 3, the quotient is 3 with a remainder of 1, and the largest integer less than or equal to 3 is 3. 

print("Modulus:", a%b) #Modulus (%) gives the remainder of the division of one number by another. For example, 10%3 will give you 1, because when you divide 10 by 3, the quotient is 3 with a remainder of 1.

print("Exponentiation:", a**b) #Exponentiation (**) is used to raise a number to the power of another number. For example, 2**3 will give you 8, because 2 raised to the power of 3 is 8.





# 2. Comparison Operators: These operators compare two values and return a boolean result (True or False).

# Example of Comparison Operators

x = 10
y = 5
print("Equal to:", x == y) #Equal to (==) checks if two values are equal. For example, 10 == 5 will return False, because 10 is not equal to 5.

print("Not equal to:", x != y) #Not equal to (!=) checks if two values are not equal. For example, 10 != 5 will return True, because 10 is not equal to 5.

print("Greater than:", x > y) #Greater than (>) checks if the left value

print("Less than:", x < y) #Less than (<) checks if the left value is less than the right value. For example, 10 < 5 will return False, because 10 is not less than 5.

print("Greater than or equal to:", x >= y) #Greater than or equal to (>=) checks if the left value is greater than or equal to the right value. For example, 10 >= 5 will return True, because 10 is greater than 5.

print("Less than or equal to:", x <= y) #Less than or equal to (<=) checks if the left value is less than or equal to the right value. For example, 10 <= 5 will return False, because 10 is not less than or equal to 5.





# 3. Logical Operators: These operators are used to combine conditional statements.

# Example of Logical Operators

a = True
b = False

print("Logical AND:", a and b) #Logical AND (and) returns True if both operands are true, otherwise it returns False. For example, True and False will return False, because both operands are not true.

print("Logical OR:", a or b) #Logical OR (or) returns True if at least one of the operands is true, otherwise it returns False. For example, True or False will return True, because at least one operand is true.

print("Logical NOT:", not a) #Logical NOT (not) returns the opposite of the operand. For example, not True will return False, because it negates the value of True.


# 4. Assignment Operators: These operators are used to assign values to variables.

# Example of Assignment Operators

x = 10
x += 5 # x = x + 5  
print("Addition Assignment:", x) #Addition Assignment (+=) adds the right operand to the left operand and assigns the result to the left operand. For example, if x is 10, then x += 5 will make x equal to 15.

x = 10
x -= 5 # x = x - 5
print("Subtraction Assignment:", x) #Subtraction Assignment (-=) subtracts the right operand from the left operand and assigns the result to the left operand. For example, if x is 10, then x -= 5 will make x equal to 5.

x = 10
x *= 5 # x = x * 5
print("Multiplication Assignment:", x) #Multiplication Assignment (*=) multiplies the left operand by the right operand and assigns the result to the left operand. For example, if x is 10, then x *= 5 will make x equal to 50.

x = 10
x /= 5 # x = x / 5
print("Division Assignment:", x) #Division Assignment (/=) divides the left operand by the right operand and assigns the result to the left operand. For example, if x is 10, then x /= 5 will make x equal to 2.0.


# 5. Bitwise Operators: These operators perform bit-level operations on binary numbers.

# Example of Bitwise Operators

a = 5  # In binary: 0101
b = 3  # In binary: 0011
print("Bitwise AND:", a & b) #Bitwise AND (&) compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, it is set to 0. For example, 5 & 3 will give you 1, because in binary, 0101 & 0011 results in 0001.

print("Bitwise OR:", a | b) #Bitwise OR (|) compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1. Otherwise, it is set to 0. For example, 5 | 3 will give you 7, because in binary, 0101 | 0011 results in 0111.


# 6. Membership Operators: These operators are used to test if a sequence contains a certain

# Example of Membership Operators

my_list = [1, 2, 3, 4, 5]
print("Membership in list:", 3 in my_list) #Membership Operator (in) checks if a value is present in a sequence (like a list, tuple, or string). For example, 3 in my_list will return True, because 3 is an element of the list [1, 2, 3, 4, 5].

message ='Radha Rani always helps others'
print("Membership in string:", 'Rani' in message) #For example, 'Rani' in message will return True, because the substring 'Rani' is present in the string "Radha Rani always helps others".


# 7. Identity Operators: These operators are used to compare the memory locations of two objects.

# Example of Identity Operators

a = [1, 2, 3]
b = a  # b references the same list as a

print("Identity check (is):", a is b) #Identity Operator (is) checks if two variables refer to the same object in memory. For example, a is b will return True, because both a and b reference the same list object in memory.

c = [1, 2, 3]  # c is a new list with the same content as a
print("Identity check (is):", a is c) #For example, a is c will return False, because a and c are different objects in memory, even though they have the same content.

a = 20
b = 20
print("Identity check (is):", a is b)

