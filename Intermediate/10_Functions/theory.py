"""
=========================================================
PYTHON FUNCTIONS - COMPLETE THEORY
=========================================================

WHAT IS A FUNCTION?

A function is a reusable block of code that performs a
specific task.

Instead of writing the same code multiple times,
we create a function once and call it whenever needed.

Benefits:
1. Code reusability
2. Better organization
3. Easier debugging
4. Reduced duplication
5. Improved readability

=========================================================
1. BASIC FUNCTION SYNTAX
=========================================================
"""

def greet():
    print("Namste Ji.")

greet()

"""
Output:
Namste Ji.

Explanation:
def -> keyword used to create function

greet -> function name

() -> parentheses for parameters

: -> start of function body

Function runs only when called.
"""


"""
=========================================================
2. FUNCTION WITH PARAMETERS
=========================================================
"""

def greet_user(name):
    print("Hello",name)

greet_user("Radha")

"""
Parameters:
Variables inside function definition.

Arguments:
Actual values passed during function call.
"""


"""
=========================================================
3. MULTIPLE PARAMETERS
=========================================================
"""

def sum(num1,num2):
    sum = num1 + num2
    print(f"sum of {num1} and {num2} is: {sum}")

sum(12,13)




"""
=========================================================
4. RETURN STATEMENT
=========================================================
"""

def division(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        print("You can't divide with zero")
        return None

divide = division(12,0)

if divide is not None:
    print(f"Division is: {divide}")

"""
return:
Returns value back to caller.

print():
Only displays output.

return makes function reusable.
"""

"""
=========================================================
5. DIFFERENCE BETWEEN PRINT AND RETURN
=========================================================
"""

def using_print():
    print("Radha Rani")

name = using_print()


def using_return():
    return "Radha Rani"

name1 = using_return()
print(name1)

"""
Output:

Radha Rani
None
Radha Rani

Explanation:

print() displays value.

return gives value back.

Function without return gives None.
"""


"""
=========================================================
6. DEFAULT PARAMETERS
=========================================================
"""

def country(name="India"):
    print(f"Your country is: {name}")

country("Korea")


"""
Output:
Korea
"""

"""
=========================================================
7. POSITIONAL ARGUMENTS
=========================================================
"""

def student(name, age):
    print(name, age)

student("Rahul", 20)


"""
Arguments passed according to position.
"""


"""
=========================================================
8. KEYWORD ARGUMENTS
=========================================================
"""

def employee(name,salary):
    print(f"You name is {name} and your salary is {salary}")

employee(salary=50000,name="Ram")

"""
Order does not matter.
"""

"""
=========================================================
9. ARBITRARY ARGUMENTS (*args)
=========================================================
"""

def numbers(*nums):
    print(nums)

numbers(10,20,30,40,50)
"""
*args stores multiple values as tuple.

Output:

(10,20,30,40)
"""



"""
=========================================================
10. KEYWORD ARBITRARY ARGUMENTS (**kwargs)
=========================================================
"""

def details(**data):
    print(f'About you {data}')

details(
    name = "Radha",
    age = 21,
    gender = "Female👧",
    city = "My heart❤️"
)

"""
Output:

About you {'name': 'Radha', 'age': 21, 'gender': 'Female👧', 'city': 'My heart❤️'}

Stored as dictionary.
"""

"""
=========================================================
11. FUNCTION WITH LIST
=========================================================
"""

def print_item(items):
    for item in items:
        print(item)

fruits = ['Apple','Banana','Grape','Papaya','Cherry']
print_item(fruits)


"""
=========================================================
12. RETURN MULTIPLE VALUES
=========================================================
"""

def calculation(num1,num2):
    return num1+num2, num1-num2, num1*num2

add,sub,multi = calculation(10,5)
print(f"Addition is {add}\nSubtraction is {sub}\nMultiplication is {multi}")

"""
Python returns tuple internally.
"""

"""
=========================================================
13. PASS STATEMENT
=========================================================
"""

def students():
    pass

"""
pass avoids syntax error.

Useful when function not implemented yet.
"""


"""
=========================================================
14. DOCSTRING
=========================================================
"""

def square(number):

    # Returns square of number

    return number*number

print(square.__doc__)


"""
Docstring explains purpose.

Useful for documentation.
"""
""""
=========================================================
15. LOCAL VARIABLE
=========================================================
"""

def information():
    name = "Radha"
    age = 21
    city = "deepk's heart💕"
    print(f"My name is {name} my age is {age} and i live in {city}")

name = 'Krishna'
age = 22
city = "my heart"

information()


"""
Local variable exists only inside function.
Local variable will be in output:
My name is Radha my age is 21 and i live in deepk's heart💕
"""

"""
=========================================================
16. GLOBAL VARIABLE
=========================================================
"""


country = "India"

def information():
    name = "Radha"
    age = 21
    city = "Deepk's heart💕"
    print(f"My name is {name} my age is {age} and i am form {country} and live in {city}")

information()

"""
Global variable accessible everywhere.
"""

count = 0

def increase():

    global count

    count += 1

increase()

print(count)


"""
global modifies global variable.
"""


"""
=========================================================
18. RECURSION
=========================================================
"""

def countdown(n):

    if n == 0:

        return

    print(n)

    countdown(n-1)

countdown(5)


"""
Function calling itself.

Output:

5
4
3
2
1
"""
"""
=========================================================
19. FACTORIAL USING RECURSION
=========================================================
"""

def factorial(n):

    if n == 1:

        return 1

    return n * factorial(n-1)

print(factorial(5))


"""
5! = 120
"""



"""
=========================================================
20. LAMBDA FUNCTION
=========================================================
"""

squares = lambda num: num*num

print(squares(5))

"""
Anonymous one-line function.
"""

"""
=========================================================
21. MAP FUNCTION
=========================================================
"""

numbers = [1,2,3,4]

result = list(map(
    lambda x:x*2,
    numbers
))
print(result)


"""
Output:

[2,4,6,8]
"""


"""
=========================================================
22. FILTER FUNCTION
=========================================================
"""

numbers=[1,2,3,4,5,6]

even=list(filter(
lambda x:x%2==0,
numbers
))

print(even)


"""
Output:

[2,4,6]
"""

"""
=========================================================
23. REDUCE FUNCTION
=========================================================
"""

from functools import reduce

numbers=[1,2,3,4]

result=reduce(
lambda a,b:a+b,
numbers
)

print(result)
"""
Output:

10
"""

"""
=========================================================
24. NESTED FUNCTION
=========================================================
"""

def outer():

    def inner():

        print("Inner")

    inner()

outer()


"""
Function inside function.
"""

"""
=========================================================
25. CLOSURE
=========================================================
"""

def outer(x):

    def inner(y):

        return x+y

    return inner

add5 = outer(5)

print(add5(10))

"""
Output:

15
"""


"""
=========================================================
26. DECORATOR BASICS
=========================================================
"""

def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper


@decorator

def hello():

    print("Hello")

hello()


"""
Decorator modifies behavior.

Output:

Before
Hello
After
"""



"""
=========================================================
27. GENERATOR FUNCTION
=========================================================
"""

def numbers():

    yield 1

    yield 2

    yield 3

for i in numbers():

    print(i)


"""
yield creates generator.

Efficient memory usage.
"""



"""
=========================================================
28. VARIABLE SCOPE (LEGB RULE)
=========================================================

L = Local

E = Enclosing

G = Global

B = Built-in

Python searches variables in this order.
"""

"""
=========================================================
29. BUILT-IN FUNCTIONS
=========================================================

Examples:

print()

len()

max()

min()

sum()

sorted()

type()

input()

range()

id()

abs()

round()

"""

"""
=========================================================
30. HIGHER ORDER FUNCTION
=========================================================
"""

def operate(func,a,b):

    return func(a,b)

def add(a,b):

    return a+b

print(
operate(
add,
10,
20
)
)


"""
Higher-order function:

Takes function as parameter
OR

Returns function
"""


"""
=========================================================
IMPORTANT INTERVIEW QUESTIONS

1. print vs return

2. *args vs **kwargs

3. local vs global

4. recursion

5. lambda

6. closure

7. decorator

8. generator

9. scope

10. higher-order functions

=========================================================

FUNCTION COMPLETE
=========================================================
"""


