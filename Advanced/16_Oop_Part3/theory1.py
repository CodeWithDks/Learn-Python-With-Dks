"""
=========================================================
PYTHON OOP (OBJECT ORIENTED PROGRAMMING) - PART 3
ADVANCED OOP CONCEPTS
=========================================================
"""


"""
=========================================================
1. WHAT IS ABSTRACTION?
=========================================================

Abstraction means hiding the internal
implementation details and showing only
the essential features to the user.

The user knows:

WHAT an object does.

The user does NOT need to know:

HOW the object does it.

Real-world examples:

1. ATM Machine
   - Withdraw money
   - Check balance

2. Car
   - Start the engine
   - Drive the car

3. Mobile Phone
   - Make calls
   - Send messages

The internal working remains hidden.
"""


"""
=========================================================
2. WHY ABSTRACTION?
=========================================================

Without abstraction:

- Systems become complex.
- Users deal with unnecessary details.
- Maintenance becomes difficult.

With abstraction:

1. Reduces complexity.
2. Improves maintainability.
3. Enhances security.
4. Provides cleaner design.
5. Focuses on essential behavior.
"""


"""
=========================================================
3. ABSTRACT CLASSES
=========================================================

An abstract class is a class that cannot
be instantiated directly.

It acts as a blueprint for other classes.

Python provides abstract classes using:

abc module

ABC stands for:

Abstract Base Class
"""

from abc import ABC

class Shape(ABC):

    pass

"""
Shape is now an abstract base class.
"""


"""
=========================================================
4. ABSTRACT METHODS
=========================================================

Abstract methods are methods declared
without implementation.

Child classes MUST implement them.

Python provides abstract methods using:

@abstractmethod
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print("Calculating circle area")

circle = Circle()
circle.area()

"""
Output:

Calculating circle area
"""


"""
Trying to create:

shape = Shape()

will raise TypeError.

Because abstract classes cannot
be instantiated directly.
"""


"""
=========================================================
5. REAL-WORLD EXAMPLE OF ABSTRACTION
=========================================================
"""

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Paid using UPI")

credit = CreditCard()

upi = UPI()
credit.pay()
upi.pay()


"""
Output:

Paid using Credit Card
Paid using UPI
"""


"""
The customer only knows:

pay()

The internal payment processing
remains hidden.
"""


"""
=========================================================
6. isinstance()
=========================================================

isinstance() checks whether an object
belongs to a particular class.

Syntax:

isinstance(object, class)
"""

class Animal:

    pass

class Dog(Animal):

    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, str))


"""
Output:

True
True
False
"""


"""
Useful when validating object types.
"""


"""
=========================================================
7. issubclass()
=========================================================

issubclass() checks whether one class
inherits from another class.

Syntax:

issubclass(child_class, parent_class)
"""


class Animal:

    pass

class Dog(Animal):

    pass

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))


"""
Output:

True
False
"""


"""
Dog is a subclass of Animal.

Animal is NOT a subclass of Dog.
"""


"""
=========================================================
8. METHOD RESOLUTION ORDER (MRO)
=========================================================

MRO determines the order in which
Python searches for methods.

It becomes important in
multiple inheritance.

Python follows:

C3 Linearization Algorithm.
"""

class A:

    pass

class B(A):

    pass

class C(A):

    pass

class D(B, C):

    pass

print(D.mro())

"""
Output:

[<class '__main__.D'>,
 <class '__main__.B'>,
 <class '__main__.C'>,
 <class '__main__.A'>,
 <class 'object'>]
"""


"""
Python searches methods in this order:

D → B → C → A → object
"""


"""
=========================================================
9. super() WITH MULTIPLE INHERITANCE
=========================================================

super() follows the Method Resolution
Order (MRO).

It does NOT simply call the immediate
parent class.
"""

class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")
        super().show()

class C(A):

    def show(self):
        print("C")
        super().show()

class D(B, C):

    def show(self):
        print("D")
        super().show()

d = D()
d.show()


"""
Output:

D
B
C
A
"""


"""
The execution follows the MRO:

D → B → C → A
"""

"""
=========================================================
10. COMPOSITION
=========================================================

Composition represents a HAS-A
relationship.

One class contains another class
as an attribute.

Example:

Car HAS-A Engine

Composition is preferred when
objects work together.
"""

class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is Running")

car = Car()
car.start_car()


"""
Output:

Engine Started
Car is Running
"""


"""
Composition promotes:

1. Code Reusability
2. Flexibility
3. Better Design

It is often preferred over
deep inheritance hierarchies.
"""