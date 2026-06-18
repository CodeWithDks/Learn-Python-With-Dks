"""
=========================================================
PYTHON OOP (OBJECT ORIENTED PROGRAMMING) - PART 2
CORE OOP PRINCIPLES
=========================================================
"""

"""
=========================================================
1. WHAT IS INHERITANCE?
=========================================================

Inheritance allows one class to acquire the
properties and methods of another class.

Parent Class → Base Class → Super Class

Child Class → Derived Class → Sub Class

Purpose:

Code Reusability

Real-world example:

Animal → Dog

Vehicle → Car
"""

"""
=========================================================
2. WHY INHERITANCE?
=========================================================

Without inheritance:

- Code duplication increases.
- Maintenance becomes difficult.

With inheritance:

1. Reusability
2. Extensibility
3. Better organization
4. Reduced redundancy
"""

"""
=========================================================
3. SINGLE INHERITANCE
=========================================================
"""

class Animal:

    def eat(self):
        print("Animal can eat")

class Dog(Animal):

    def bark(self):
        print("Dog can bark")

dog = Dog()
dog.eat()
dog.bark()

"""
Output:

Animal can eat
Dog can bark
"""

"""
=========================================================
4. MULTILEVEL INHERITANCE
=========================================================
"""

class Grandparent:

    def show1(self):
        print("Grandparent")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass


child = Child()
child.show1()

"""
Output:

Grandparent
"""

"""
=========================================================
5. MULTIPLE INHERITANCE
=========================================================
"""

class Father:

    def skill1(self):
        print("Driving")

class Mother:

    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skill1()
child.skill2()


"""
Output:

Driving
Cooking
"""

"""
=========================================================
6. HIERARCHICAL INHERITANCE
=========================================================
"""

class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
dog.eat()
cat.eat()

"""
=========================================================
7. HYBRID INHERITANCE
=========================================================

Hybrid inheritance is a combination of
two or more inheritance types.

Python supports hybrid inheritance.

It is usually achieved using
multiple inheritance.
"""

"""
=========================================================
8. METHOD OVERRIDING
=========================================================
"""

class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

"""
Output:

Dog barks
"""

"""
=========================================================
9. super() FUNCTION
=========================================================

super() is used to access the parent
class methods and constructor.
"""

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student = Student("Deepak", "Python")

print(student.name)
print(student.course)

"""
Output:
Deepak
Python
"""

"""
=========================================================
10. WHAT IS POLYMORPHISM?
=========================================================

Poly = Many

Morph = Forms

Polymorphism means one interface
can have many forms.

Example:

The same method behaves differently
for different objects.
"""

"""
=========================================================
11. POLYMORPHISM USING METHOD OVERRIDING
=========================================================
"""

class Bird:

    def fly(self):
        print("Bird flies")

class Penguin(Bird):

    def fly(self):
        print("Penguin cannot fly")

birds = [Bird(), Penguin()]
for bird in birds:
    bird.fly()

"""
=========================================================
12. DUCK TYPING
=========================================================

"If it walks like a duck and quacks
like a duck, it is a duck."

Python focuses on behavior rather
than object type.
"""

class Duck:

    def speak(self):
        print("Quack")

class Human:

    def speak(self):
        print("Hello")

def call_speak(obj):
    obj.speak()

call_speak(Duck())
call_speak(Human())

"""
=========================================================
13. INTRODUCTION TO OPERATOR OVERLOADING
=========================================================

Operator overloading means giving
special meaning to operators for
user-defined objects.

Example:

+ operator

== operator

< operator
"""

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)

"""
Output:
30
"""

"""
=========================================================
14. WHAT IS ENCAPSULATION?
=========================================================

Encapsulation means binding data and
methods together into a single unit.

It also helps restrict direct access
to some data.
"""

"""
=========================================================
15. PUBLIC MEMBERS
=========================================================

Public members can be accessed from
anywhere.
"""

class Student:

    def __init__(self):
        self.name = "Deepak"

student = Student()
print(student.name)

"""
=========================================================
16. PROTECTED MEMBERS
=========================================================

Protected members start with a
single underscore (_).

Convention:

They should not be accessed outside
the class hierarchy.
"""

class Student:

    def __init__(self):
        self._course = "Python"

student = Student()
print(student._course)

"""
=========================================================
17. PRIVATE MEMBERS
=========================================================

Private members start with double
underscores (__).

They cannot be directly accessed
outside the class.
"""

class Student:

    def __init__(self):
        self.__salary = 50000

student = Student()
# print(student.__salary)

"""
Raises AttributeError
"""

"""
=========================================================
18. NAME MANGLING
=========================================================

Python internally changes:

__variable

to

_ClassName__variable

This is called Name Mangling.
"""

class Student:

    def __init__(self):
        self.__salary = 50000

student = Student()
print(student._Student__salary)

"""
Output:

50000
"""

"""
=========================================================
19. COMMON BEGINNER MISTAKES
=========================================================

1. Confusing inheritance types.

2. Forgetting to use super().

3. Thinking private variables are
   completely inaccessible.

4. Overusing inheritance.

5. Confusing overriding with
   overloading.
"""

"""
=========================================================
20. BEST PRACTICES
=========================================================

1. Prefer composition over deep
   inheritance chains.

2. Use inheritance only when there
   is an "IS-A" relationship.

3. Use super() properly.

4. Keep encapsulation meaningful.

5. Write clear and maintainable
   class hierarchies.
"""

"""
=========================================================
21. INTERVIEW QUESTIONS
=========================================================

1. What is inheritance?

2. Why do we use inheritance?

3. Explain single inheritance.

4. Explain multiple inheritance.

5. What is method overriding?

6. What is super()?

7. What is polymorphism?

8. What is duck typing?

9. What is encapsulation?

10. Difference between public,
    protected, and private members?

11. What is name mangling?

12. What is operator overloading?
"""

"""
=========================================================
22. FINAL SUMMARY
=========================================================

Core OOP concepts learned:

✓ Inheritance

✓ Single Inheritance

✓ Multilevel Inheritance

✓ Multiple Inheritance

✓ Hierarchical Inheritance

✓ Hybrid Inheritance

✓ Method Overriding

✓ super()

✓ Polymorphism

✓ Duck Typing

✓ Operator Overloading

✓ Encapsulation

✓ Public Members

✓ Protected Members

✓ Private Members

✓ Name Mangling

These concepts are essential for
building reusable and maintainable
object-oriented applications.

Next Part:

Abstraction, Abstract Classes,
Magic Methods, Property Decorators,
Data Classes, Composition,
Aggregation, and Method Resolution
Order (MRO).
"""