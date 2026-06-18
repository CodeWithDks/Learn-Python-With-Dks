# ==========================================================
# DAY 17 - ITERATORS & GENERATORS
# ==========================================================

# ==========================================================
# 1. WHAT IS AN ITERABLE?
# ==========================================================

"""
An iterable is any object that can be looped through.

Examples:
- List
- Tuple
- String
- Set
- Dictionary

Python uses iterables inside loops.
"""

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# ==========================================================
# 2. WHAT IS AN ITERATOR?
# ==========================================================

"""
An iterator is an object that remembers its current position
while traversing data.

It returns one value at a time.

Iterator contains:
1. __iter__()
2. __next__()

Every iterator is iterable.

But every iterable is NOT an iterator.
"""


# ==========================================================
# 3. ITERABLE VS ITERATOR
# ==========================================================

"""
Iterable:
--------
Can be looped over.

Examples:
list
tuple
string
dictionary

Iterator:
---------
Produces values one by one using next().
Keeps track of current position.
"""

my_list = [1, 2, 3]

print(type(my_list))

iterator = iter(my_list)

print(type(iterator))


# ==========================================================
# 4. iter()
# ==========================================================

"""
iter() converts an iterable into an iterator.
"""

numbers = [100, 200, 300]

it = iter(numbers)

print(it)


# ==========================================================
# 5. next()
# ==========================================================

"""
next() gets the next value from an iterator.
"""

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


# ==========================================================
# 6. STOPITERATION EXCEPTION
# ==========================================================

"""
When no values remain,
next() raises StopIteration.
"""

numbers = [1, 2]

it = iter(numbers)

print(next(it))
print(next(it))

# print(next(it))
# StopIteration


# ==========================================================
# 7. HANDLING STOPITERATION
# ==========================================================

numbers = [10, 20]

it = iter(numbers)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("Iterator Finished")
        break


# ==========================================================
# 8. HOW FOR LOOP WORKS INTERNALLY
# ==========================================================

"""
for loop internally uses:

1. iter()
2. next()

Example:
"""

numbers = [1, 2, 3]

it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break


# ==========================================================
# 9. CUSTOM ITERATOR
# ==========================================================

"""
We can create our own iterator using a class.
"""

class Counter:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


obj = Counter(1, 5)

for i in obj:
    print(i)


# ==========================================================
# 10. ANOTHER CUSTOM ITERATOR EXAMPLE
# ==========================================================

class EvenNumbers:

    def __init__(self, limit):
        self.number = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.number > self.limit:
            raise StopIteration

        value = self.number
        self.number += 2

        return value


for num in EvenNumbers(10):
    print(num)


# ==========================================================
# 11. WHY GENERATORS?
# ==========================================================

"""
Problem with Iterators:

Creating iterator classes requires:
- __iter__()
- __next__()

Too much code.

Generators make it easy.

Generators automatically create iterators.
"""


# ==========================================================
# 12. WHAT IS A GENERATOR?
# ==========================================================

"""
A generator is a special function that uses
the yield keyword.

Generator returns values one at a time.

It remembers where it stopped.
"""


# ==========================================================
# 13. FIRST GENERATOR FUNCTION
# ==========================================================

def numbers():

    yield 1
    yield 2
    yield 3


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))


# ==========================================================
# 14. YIELD KEYWORD
# ==========================================================

"""
yield pauses the function
and remembers its state.

Next call resumes from where it stopped.
"""

def demo():

    print("First")
    yield 1

    print("Second")
    yield 2

    print("Third")
    yield 3


gen = demo()

print(next(gen))
print(next(gen))
print(next(gen))


# ==========================================================
# 15. YIELD VS RETURN
# ==========================================================

"""
return:
-------
Ends function immediately.

yield:
------
Pauses function.
Can continue later.
"""

def using_return():
    return 10


def using_yield():
    yield 10


print(using_return())

print(using_yield())


# ==========================================================
# 16. MULTIPLE YIELD STATEMENTS
# ==========================================================

def fruits():

    yield "Apple"
    yield "Banana"
    yield "Mango"


for fruit in fruits():
    print(fruit)


# ==========================================================
# 17. GENERATOR WITH LOOP
# ==========================================================

def count(limit):

    for i in range(1, limit + 1):
        yield i


for number in count(5):
    print(number)


# ==========================================================
# 18. GENERATOR FOR EVEN NUMBERS
# ==========================================================

def even_numbers(limit):

    for i in range(2, limit + 1, 2):
        yield i


for num in even_numbers(20):
    print(num)


# ==========================================================
# 19. GENERATOR FOR ODD NUMBERS
# ==========================================================

def odd_numbers(limit):

    for i in range(1, limit + 1, 2):
        yield i


for num in odd_numbers(15):
    print(num)


# ==========================================================
# 20. GENERATOR EXPRESSION
# ==========================================================

"""
Generator expression is similar to
list comprehension.

Syntax:

(value for item in iterable)
"""

gen = (x * x for x in range(5))

for value in gen:
    print(value)


# ==========================================================
# 21. LIST COMPREHENSION VS GENERATOR
# ==========================================================

list_data = [x * x for x in range(5)]

generator_data = (x * x for x in range(5))

print(list_data)
print(generator_data)


# ==========================================================
# 22. MEMORY EFFICIENCY
# ==========================================================

"""
List stores all values in memory.

Generator produces values when needed.

Generators are memory efficient.
"""

numbers = (x for x in range(1000000))

print(next(numbers))
print(next(numbers))
print(next(numbers))


# ==========================================================
# 23. FIBONACCI GENERATOR
# ==========================================================

def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):

        yield a

        a, b = b, a + b


for num in fibonacci(10):
    print(num)


# ==========================================================
# 24. INFINITE GENERATOR
# ==========================================================

def infinite_counter():

    num = 1

    while True:
        yield num
        num += 1


counter = infinite_counter()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


# ==========================================================
# 25. REAL WORLD EXAMPLE
# ==========================================================

"""
Imagine reading a huge file.

Instead of loading entire file into memory,
generator reads one line at a time.
"""

def read_lines():

    lines = [
        "Line 1",
        "Line 2",
        "Line 3"
    ]

    for line in lines:
        yield line


for line in read_lines():
    print(line)


# ==========================================================
# ADVANTAGES OF GENERATORS
# ==========================================================

"""
1. Less Memory Usage

2. Faster Execution

3. Suitable for Large Data

4. Produces Values Lazily

5. Easy to Write
"""


# ==========================================================
# PRACTICE PROGRAM 1
# ==========================================================

def square_generator(limit):

    for i in range(1, limit + 1):
        yield i ** 2


for num in square_generator(5):
    print(num)


# ==========================================================
# PRACTICE PROGRAM 2
# ==========================================================

class ReverseIterator:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):

        if self.index == 0:
            raise StopIteration

        self.index -= 1

        return self.data[self.index]


for value in ReverseIterator("PYTHON"):
    print(value)


# ==========================================================
# PRACTICE PROGRAM 3
# ==========================================================

def countdown(start):

    while start > 0:
        yield start
        start -= 1


for num in countdown(10):
    print(num)


# ==========================================================
# QUICK REVISION
# ==========================================================

"""
Iterable
--------
Object that can be looped over.

Iterator
--------
Object that returns values one by one.

iter()
------
Converts iterable into iterator.

next()
------
Gets next value.

StopIteration
-------------
Raised when iterator ends.

Generator
---------
Function using yield.

yield
-----
Pauses function and remembers state.

Generator Expression
--------------------
(x for x in iterable)

Benefits
--------
Memory Efficient
Fast
Easy to Create
Useful for Large Data
"""