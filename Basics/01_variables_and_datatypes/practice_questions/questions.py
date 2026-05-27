1.# Create three variables: age (int), salary (float), name (str). Print all three.
age = 20
salary = 20000.40
name = 'Ravi'
print(f"Your name is {name}, your age is {age} and your salary is {salary}$")


2. # Take a string "50", convert it to integer, and add 20 to it.
string_number ='50'
print(int(string_number)+20)

3. # Create two float numbers and print their division result.
num1 = 20.5
num2 = 3.6
print(num1/num2)

4. # Create a variable x = 25. Convert it into float and print its type.
x = 25
x_float = float(x)
print(type(x_float))

5.# Create a variable price = 99.99. Convert it into int. Print result and explain what happened.
price = 99.99
price_int = int(price)
print(price_int) # Output: 99
# Explanation: When we convert the float 99.99 to an integer using the int() function, it truncates the decimal part and only keeps the whole number. Therefore, the result is 99 instead of 100, because int() does not round the number; it simply removes the decimal portion.

6. # Create a variable name = "Python". Print the first character.
name = 'pythonn'
print(name[0])


7. # Create a string "100". Convert it to float, then multiply it by 2.
string_num = '100'
print(float(string_num)*2)

8. # Create two variables:
    
a = "Hello"
b = "World"
    
print(a + " " + b) # Output: Hello World
    
9. # Create a variable x = 5. Print:
    
# The value of x is 5
    
# (Use type conversion properly.)
x = 5
print("The value of x is " + str(x))

    
10. # Create three variables:
    
length = 5
    
width = 2.5
    
# Compute area and print result. Also print its data type.
length = 5
width = 2.5
area = length * width
print("Area:", area) # Output: Area: 12.5
print("Data type of area:", type(area)) # Output: Data type of area: <class 'float'>
