"""
=========================================================
1. __len__ METHOD
=========================================================

__len__ allows objects to work with
the built-in len() function.

It returns the length of an object.
"""

class BookCollection:

    def __init__(self, books):
        self.books = books

    def __len__(self):
        return len(self.books)

library = BookCollection(["Python", "Java", "C++"])
print(len(library))


"""
Output:

3
"""


"""
=========================================================
2. __call__ METHOD
=========================================================

__call__ allows an object to behave
like a function.

Objects become callable.
"""

class Greeter:

    def __call__(self):
        print("Hello, Welcome!")

greet = Greeter()
greet()

"""
Output:

Hello, Welcome!
"""


"""
Without __call__:

object()

Raises TypeError

With __call__:

The object behaves like a function.
"""


"""
=========================================================
3. __getitem__ METHOD
=========================================================

__getitem__ allows indexing using [].

It defines how objects respond to:

object[index]
"""


class Team:

    def __init__(self, members):
        self.members = members

    def __getitem__(self, index):
        return self.members[index]

team = Team(["Deepak", "Aman", "Rahul"])
print(team[0])
print(team[2])


"""
Output:

Deepak
Rahul
"""


"""
=========================================================
4. __contains__ METHOD
=========================================================

__contains__ defines how the 'in'
operator behaves.

Syntax:

item in object
"""

class Team:

    def __init__(self, members):
        self.members = members

    def __contains__(self, item):
        return item in self.members

team = Team(["Deepak", "Aman", "Rahul"])

print("Deepak" in team)
print("Krishna" in team)


"""
Output:

True
False
"""


"""
=========================================================
5. __slots__
=========================================================

__slots__ restricts the attributes
that objects can have.

Benefits:

1. Saves memory.
2. Prevents accidental attribute creation.
"""


class Student:

    __slots__ = ["name", "age"]

    def __init__(self, name, age):

        self.name = name
        self.age = age

student = Student("Deepak", 22)

print(student.name)
print(student.age)


"""
Output:

Deepak
22
"""


"""
Trying this:

student.course = "Python"

Raises:

AttributeError

Because 'course' is not defined
inside __slots__.
"""


"""
=========================================================
6. WHAT ARE DATACLASSES?
=========================================================

Dataclasses automatically generate
common methods like:

1. __init__()
2. __repr__()
3. __eq__()

Python provides dataclasses using:

dataclasses module

They reduce boilerplate code.
"""

from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int

student = Student("Deepak", 22)
print(student)

"""
Output:

Student(name='Deepak', age=22)
"""

"""
=========================================================
7. DEFAULT VALUES IN DATACLASSES
=========================================================

Dataclass fields can have default values.
"""

from dataclasses import dataclass

@dataclass
class Student:

    name: str
    age: int = 18

student = Student("Deepak")
print(student)


"""
Output:

Student(name='Deepak', age=18)
"""


"""
=========================================================
8. FROZEN DATACLASSES
=========================================================

Frozen dataclasses create immutable
objects.

Their attributes cannot be modified.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Student:

    name: str
    age: int

student = Student("Deepak", 22)
print(student)


"""
Output:

Student(name='Deepak', age=22)
"""


"""
Trying this:

student.age = 23

Raises:

FrozenInstanceError
"""


"""
=========================================================
9. COMMON BEGINNER MISTAKES
=========================================================

1. Overusing inheritance.

2. Forgetting to implement abstract
   methods.

3. Confusing Composition with
   Aggregation.

4. Misusing property decorators.

5. Forgetting that __eq__ changes
   equality behavior.

6. Using __slots__ without understanding
   its limitations.

7. Overcomplicating class hierarchies.

8. Ignoring dataclasses when they
   simplify code.
"""


"""
=========================================================
10. BEST PRACTICES
=========================================================

1. Prefer Composition over deep
   inheritance.

2. Use Abstraction to define contracts.

3. Use Encapsulation to protect data.

4. Use @property for controlled access.

5. Use dataclasses for data-heavy classes.

6. Keep classes focused on a single
   responsibility.

7. Write readable and maintainable code.

8. Understand special methods before
   overriding them.
"""


"""
=========================================================
11. INTERVIEW QUESTIONS
=========================================================

1. What is abstraction?

2. What is an abstract class?

3. Difference between abstraction and
   encapsulation?

4. What is MRO?

5. What is Composition?

6. Difference between Composition and
   Aggregation?

7. Why use @property?

8. What are getters and setters?

9. Explain __eq__.

10. Explain __len__.

11. Explain __call__.

12. Explain __getitem__.

13. Explain __contains__.

14. What is __slots__?

15. What are dataclasses?

16. Advantages of dataclasses?

17. What are frozen dataclasses?

18. Composition vs Inheritance?
"""


"""
=========================================================
12. FINAL SUMMARY
=========================================================

Advanced OOP concepts learned:

✓ Abstraction

✓ Abstract Classes

✓ Abstract Methods

✓ isinstance()

✓ issubclass()

✓ Method Resolution Order (MRO)

✓ super() with Multiple Inheritance

✓ Composition

✓ Aggregation

✓ Composition vs Inheritance

✓ Getters and Setters

✓ @property

✓ @setter

✓ @deleter

✓ __eq__

✓ __len__

✓ __call__

✓ __getitem__

✓ __contains__

✓ __slots__

✓ Dataclasses

✓ Default Values in Dataclasses

✓ Frozen Dataclasses


You have now completed the complete
Python OOP roadmap.

Part 1:
- OOP Foundations

Part 2:
- Core OOP Principles

Part 3:
- Advanced OOP Concepts


These concepts are widely used in:

- Web Development
- Desktop Applications
- APIs
- Automation
- Large Python Projects


Next Topics:

Day 17 → Iterators & Generators

Day 18 → Decorators

Day 19 → Regular Expressions

Day 20 → JSON & APIs

Day 21 → SQLite Database


Congratulations!

You have successfully completed
Python OOP from beginner to
advanced level.
"""