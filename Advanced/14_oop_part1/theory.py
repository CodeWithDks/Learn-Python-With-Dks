"""
=========================================================
PYTHON OOP (OBJECT ORIENTED PROGRAMMING) - PART 1
=========================================================
"""

"""
=========================================================
1. WHAT IS OOP?
=========================================================

OOP stands for Object-Oriented Programming.

It is a programming paradigm that organizes code
using Classes and Objects.

Instead of focusing only on functions, OOP focuses on:

1. Data
2. Behavior

Real-world examples:

Car
Student
Employee
Bank Account
Mobile Phone

Everything can be represented as objects.
"""

"""
=========================================================
2. WHY OOP IS IMPORTANT?
=========================================================

Without OOP:

- Code becomes repetitive
- Large projects become difficult to manage

With OOP:

1. Reusability
2. Maintainability
3. Scalability
4. Better organization

OOP is heavily used in:

- Web Development
- Game Development
- Desktop Applications
- APIs
"""

"""
=========================================================
3. WHAT IS A CLASS?
=========================================================

A class is a blueprint for creating objects.

Think:

Blueprint -> House

Class -> Object

A class defines:

1. Attributes (Data)
2. Methods (Behavior)
"""

"""
=========================================================
4. CREATING A CLASS
=========================================================
"""

class Student:

    pass


"""
Student is a class.

pass means:

Do nothing.
"""

"""
=========================================================
5. WHAT IS AN OBJECT?
=========================================================

An object is an instance of a class.

Example:

Class -> Student

Objects:

student1
student2
student3
"""

"""
=========================================================
6. CREATING OBJECTS
=========================================================
"""

class Student:
    pass

student1 = Student()
student2 = Student()

print(student1)
print(student2)

"""
Each object has its own memory location.
"""

"""
=========================================================
7. CONSTRUCTOR (__init__)
=========================================================
"""

class Student:

    def __init__(self):

        print("Object Created")


student1 = Student()


"""
Output:

Object Created
__init__ runs automatically when object is created.
"""

"""
=========================================================
8. UNDERSTANDING self
=========================================================

self refers to the current object.
It allows objects to access their own data.
Python automatically passes self.
"""

"""
=========================================================
9. INSTANCE VARIABLES
=========================================================
"""

class Student:

    def __init__(self):

        self.name = "Deepak"
        self.age = 21

student1 = Student()

print(student1.name)
print(student1.age)

"""
Output:

Deepak
21
"""

"""
=========================================================
10. PASSING VALUES TO CONSTRUCTOR
=========================================================
"""

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student1 = Student("Deepak", 22)

print(student1.name)
print(student1.age)

"""
Output:

Deepak
22
"""

"""
=========================================================
11. INSTANCE METHODS
=========================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


student1 = Student("Deepak")
student1.display()

"""
Output:

Name: Deepak
"""

"""
=========================================================
12. MULTIPLE OBJECTS
=========================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Radha")
student2 = Student("Krishna")

print(student1.name)
print(student2.name)

"""
Output:

Radha
Krishna
"""

"""
=========================================================
13. MODIFYING OBJECT ATTRIBUTES
=========================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Deepak")
student1.name = "Aman"

print(student1.name)

