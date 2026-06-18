"""
=========================================================
1. AGGREGATION
=========================================================

Aggregation represents a HAS-A relationship.

It is a weaker form of Composition.

In Aggregation:

- Objects can exist independently.
- One object uses another object.

Real-world example:

Department HAS-A Teacher

Teacher can exist even if the
Department is deleted.
"""


class Teacher:

    def __init__(self, name):
        self.name = name

class Department:

    def __init__(self, teacher):
        self.teacher = teacher

    def display_teacher(self):
        print("Teacher:", self.teacher.name)


teacher = Teacher("Deepak")
department = Department(teacher)
department.display_teacher()

"""
Output:

Teacher: Deepak
"""

"""
=========================================================
2. COMPOSITION VS INHERITANCE
=========================================================

Inheritance:

Represents an IS-A relationship.

Example:

Dog IS-A Animal


Composition:

Represents a HAS-A relationship.

Example:

Car HAS-A Engine


Use Inheritance when:

- Specialization is required.

Use Composition when:

- Objects collaborate together.

Composition is often preferred because
it provides greater flexibility.
"""


"""
=========================================================
3. GETTERS AND SETTERS
=========================================================

Getters:

Methods used to access private data.

Setters:

Methods used to modify private data.

They provide controlled access to
object attributes.
"""

class Student:

    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

        else:
            print("Invalid Age")


student = Student()
student.set_age(22)
print(student.get_age())


"""
Output:

22
"""


"""
=========================================================
4. PROPERTY DECORATOR (@property)
=========================================================

@property allows a method to behave
like an attribute.

It provides a Pythonic way to
implement getters.
"""

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks


student = Student(90)
print(student.marks)


"""
Output:

90
"""


"""
Without @property:

student.marks()

With @property:

student.marks
"""


"""
=========================================================
5. PROPERTY SETTER (@setter)
=========================================================

@setter allows controlled modification
of attributes.

Syntax:

@attribute_name.setter
"""

class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):

        if 0 <= value <= 100:
            self._marks = value

        else:
            print("Invalid Marks")


student = Student(85)
student.marks = 95
print(student.marks)


"""
Output:

95
"""

student.marks = 120

"""
Output:

Invalid Marks
"""


"""
=========================================================
6. PROPERTY DELETER (@deleter)
=========================================================

@deleter defines what happens when
an attribute is deleted.

Syntax:

@attribute_name.deleter
"""

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name")
        del self._name


student = Student("Deepak")
print(student.name)
del student.name


"""
Output:

Deepak
Deleting name
"""


"""
=========================================================
7. ADVANCED OPERATOR OVERLOADING (__eq__)
=========================================================

__eq__ overloads the == operator.

It defines how objects should be
compared for equality.
"""

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks


student1 = Student(90)
student2 = Student(90)
student3 = Student(80)

print(student1 == student2)
print(student1 == student3)


"""
Output:

True
False
"""


"""
Without __eq__:

Python compares memory locations.

With __eq__:

Python compares object data.
"""