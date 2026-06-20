# ==========================================================
# DAY 18 - DECORATORS
# ==========================================================

# ==========================================================
# 1. FUNCTIONS ARE FIRST-CLASS OBJECTS
# ==========================================================

"""
In Python, functions are treated as objects.

This means:
1. Functions can be assigned to variables.
2. Functions can be passed as arguments.
3. Functions can be returned from other functions.
"""

def greet():
    print("Hello World")

say_hello = greet
say_hello()


# ==========================================================
# 2. ASSIGNING FUNCTION TO A VARIABLE
# ==========================================================

def add(a, b):
    return a + b


sum_function = add
print(sum_function(10, 20))


# ==========================================================
# 3. PASSING FUNCTION AS AN ARGUMENT
# ==========================================================

def greet():
    print("Welcome")


def execute(function):
    function()

execute(greet)


# ==========================================================
# 4. FUNCTION INSIDE FUNCTION
# ==========================================================

def outer():

    def inner():
        print("Inside Inner Function")
    inner()

outer()


# ==========================================================
# 5. RETURNING A FUNCTION
# ==========================================================

def outer():

    def inner():
        print("Returned Function")
    return inner

result = outer()

result()


# ==========================================================
# 6. INTRODUCTION TO CLOSURES
# ==========================================================

"""
A closure remembers variables from its outer scope
even after the outer function has finished executing.
"""

def outer():

    message = "Hello Python"

    def inner():
        print(message)
    return inner

result = outer()

result()


# ==========================================================
# 7. ANOTHER CLOSURE EXAMPLE
# ==========================================================

def multiplier(x):

    def multiply(y):
        return x * y
    return multiply


double = multiplier(2)
print(double(10))
triple = multiplier(3)
print(triple(10))


# ==========================================================
# 8. WHAT IS A DECORATOR?
# ==========================================================

"""
A decorator is a function that adds extra functionality
to another function without modifying its original code.

Decorators use closures internally.
"""

# ==========================================================
# 9. BASIC DECORATOR STRUCTURE
# ==========================================================

def decorator_function(original_function):

    def wrapper():
        print("Before Function Execution")
        original_function()
        print("After Function Execution")
    return wrapper


def display():
    print("Display Function")


decorated = decorator_function(display)

decorated()


# ==========================================================
# 10. DECORATOR USING @ SYMBOL
# ==========================================================

def decorator_function(original_function):

    def wrapper():
        print("Before Function")
        original_function()
        print("After Function")
    return wrapper


@decorator_function
def hello():
    print("Hello Python")


hello()


# ==========================================================
# 11. WHY USE DECORATORS?
# ==========================================================

"""
Without decorators:

You may repeat the same code in multiple functions.

With decorators:

Write the extra functionality once
and reuse it everywhere.
"""

# ==========================================================
# 12. DECORATOR EXAMPLE - LOGGING
# ==========================================================

def logger(function):

    def wrapper():
        print("Function Started")
        function()
        print("Function Ended")
    return wrapper


@logger
def show_data():
    print("Displaying Data")


show_data()


# ==========================================================
# 13. DECORATOR WITH PARAMETERS
# ==========================================================

def decorator_function(function):

    def wrapper(*args):

        print("Before Function")
        function(*args)
        print("After Function")
    return wrapper


@decorator_function
def greet(name):
    print("Hello", name)


greet("Deepak")


# ==========================================================
# 14. *args IN DECORATORS
# ==========================================================

"""
*args allows any number of positional arguments.
"""

def decorator_function(function):

    def wrapper(*args):
        print("Executing Function")
        function(*args)
    return wrapper


@decorator_function
def add(a, b):
    print(a + b)

add(5, 10)


# ==========================================================
# 15. **kwargs IN DECORATORS
# ==========================================================

"""
**kwargs allows any number of keyword arguments.
"""

def decorator_function(function):

    def wrapper(*args, **kwargs):
        print("Before Execution")
        function(*args, **kwargs)
    return wrapper


@decorator_function
def student(name, age):
    print(name, age)


student(name="Deepak", age=21)


# ==========================================================
# 16. RETURN VALUES IN DECORATORS
# ==========================================================

def decorator_function(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result
    return wrapper


@decorator_function
def multiply(a, b):
    return a * b

print(multiply(5, 4))


# ==========================================================
# 17. PRACTICAL EXAMPLE - AUTHENTICATION
# ==========================================================

def login_required(function):

    def wrapper():

        is_logged_in = True

        if is_logged_in:
            function()
        else:
            print("Please Login First")
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()


# ==========================================================
# 18. PRACTICAL EXAMPLE - ACCESS CONTROL
# ==========================================================

def admin_required(function):

    def wrapper():

        role = "admin"
        if role == "admin":
            function()
        else:
            print("Access Denied")
    return wrapper

@admin_required
def delete_user():
    print("User Deleted")


delete_user()


# ==========================================================
# 19. MULTIPLE DECORATORS
# ==========================================================

def decorator_one(function):

    def wrapper():
        print("Decorator One Start")
        function()
        print("Decorator One End")
    return wrapper


def decorator_two(function):

    def wrapper():
        print("Decorator Two Start")
        function()
        print("Decorator Two End")
    return wrapper


@decorator_one
@decorator_two
def display():
    print("Display Function")

display()


# ==========================================================
# 20. ORDER OF DECORATOR EXECUTION
# ==========================================================

"""
Execution Order:

@decorator_one
@decorator_two

Equivalent To:

decorator_one(
    decorator_two(display)
)

Bottom decorator executes first.
"""

# ==========================================================
# 21. BUILT-IN DECORATOR - @staticmethod
# ==========================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))


# ==========================================================
# 22. WHY @staticmethod?
# ==========================================================

"""
Use @staticmethod when:

Method does not need:
1. self
2. class variables

It behaves like a normal function
inside a class.
"""

# ==========================================================
# 23. BUILT-IN DECORATOR - @classmethod
# ==========================================================

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()


# ==========================================================
# 24. WHY @classmethod?
# ==========================================================

"""
Use @classmethod when:

You need access to class variables.

cls refers to the class itself.
"""

# ==========================================================
# 25. BUILT-IN DECORATOR - @property
# ==========================================================

class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Deepak")
print(p.name)


# ==========================================================
# 26. WHY @property?
# ==========================================================

"""
Allows method access like an attribute.

Without @property:

obj.name()

With @property:

obj.name
"""

# ==========================================================
# 27. PROPERTY SETTER
# ==========================================================

class Employee:

    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            print("Invalid Salary")
        else:
            self._salary = value


emp = Employee()
emp.salary = 50000
print(emp.salary)


# ==========================================================
# 28. PROPERTY DELETER
# ==========================================================

class User:

    def __init__(self):
        self._name = "Deepak"

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Name Deleted")
        del self._name

user = User()
del user.name


# ==========================================================
# 29. DECORATOR EXAMPLE - EXECUTION TIMER
# ==========================================================

import time


def timer(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return wrapper


@timer
def task():

    time.sleep(2)
    print("Task Completed")


task()


# ==========================================================
# 30. DECORATOR EXAMPLE - FUNCTION CALL COUNTER
# ==========================================================

def count_calls(function):

    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Function Called", count, "Times")
        function()
    return wrapper


@count_calls
def hello():
    print("Hello")


hello()
hello()
hello()


# ==========================================================
# 31. DECORATOR EXAMPLE - INPUT VALIDATION
# ==========================================================

def positive_number(function):

    def wrapper(number):
        if number < 0:
            print("Only Positive Numbers Allowed")
            return
        return function(number)
    return wrapper


@positive_number
def square(number):
    print(number ** 2)


square(5)
square(-5)


# ==========================================================
# ADVANTAGES OF DECORATORS
# ==========================================================

"""
1. Code Reusability

2. Cleaner Code

3. Easier Maintenance

4. Add Functionality Without
   Changing Original Function

5. Used Widely In:
   - Django
   - Flask
   - FastAPI
   - Logging
   - Authentication
   - Authorization
   - Performance Monitoring
"""

# ==========================================================
# QUICK REVISION
# ==========================================================

"""
Function as First-Class Object
------------------------------
Functions can be assigned, passed,
and returned.

Closure
-------
Inner function remembers outer variables.

Decorator
---------
Adds functionality to another function.

@ Symbol
---------
Used to apply decorators.

*args
-----
Accepts multiple positional arguments.

**kwargs
--------
Accepts multiple keyword arguments.

Built-In Decorators
-------------------
@staticmethod
@classmethod
@property

Benefits
--------
Reusable
Clean
Powerful
Professional
"""