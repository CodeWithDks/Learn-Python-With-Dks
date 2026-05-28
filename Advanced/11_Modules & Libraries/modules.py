""" 
=========================================================
PYTHON MODULES - COMPLETE THEORY 
========================================================= 
"""

"""
=========================================================
1. WHAT IS A MODULE?
=========================================================

A module is simply a Python file containing Python code.

Example:

calculator.py

This file itself becomes a module.

Modules help us:

1. Organize code
2. Reuse code
3. Avoid duplication
4. Make programs cleaner
5. Divide large projects into smaller parts
"""

"""
=========================================================
2. WHY MODULES ARE IMPORTANT
=========================================================

Imagine writing everything in one file:

- login system
- database code
- payment system
- API code

Everything becomes difficult to manage.

Modules solve this problem by separating code into files.
"""

"""
=========================================================
3. CREATING YOUR FIRST MODULE
=========================================================
"""

# File: math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a,b):
    return a * b

"""
This file now becomes a module.
"""

"""
=========================================================
4. IMPORTING MODULE
=========================================================
"""

# File: main.py

import math_utils

print(math_utils.add(10, 5))
print(math_utils.subtract(20, 10))
print(math_utils.multiplication(20,5))

"""
Output:

15
10
100
"""

"""
=========================================================
5. UNDERSTANDING NAMESPACE
=========================================================

math_utils.add()

Here:

math_utils -> namespace

Namespaces prevent naming conflicts.

Example:

module1.add()

module2.add()

Both functions can safely exist.
"""

"""
=========================================================
6. IMPORT SPECIFIC FUNCTION
=========================================================
"""

from math_utils import add

addition = add(5,5)
print("Addition is: ",addition)

"""
Output:

10
25
"""


"""
=========================================================
7. IMPORT MULTIPLE FUNCTIONS
=========================================================
"""

from math_utils import add, subtract

print(add(2,3))

print(subtract(10,5))


"""
Output:

5
5
"""

"""
=========================================================
8. IMPORT EVERYTHING (*)
=========================================================
"""

from math_utils import *


"""
BAD PRACTICE.

Why?

1. Namespace pollution
2. Hard debugging
3. Naming conflicts
4. Poor readability

Professional developers avoid this.
"""

"""
=========================================================
9. ALIASING MODULES
=========================================================
"""

import math as m

print(m.sqrt(25))
print(m.factorial(5))
print(m.copysign(100,200))

"""
Output:

5.0
120
100.0
"""

"""
=========================================================
10. FUNCTION ALIASING
=========================================================
"""

from math import factorial as fact
from math import sqrt as s 

print(fact(3))
print(s(25))


"""
Output:
6
5.0
"""

"""
=========================================================
11. BUILT-IN MODULES
=========================================================

Python already provides many built-in modules.

Examples:

math
random
datetime
os
sys
platform
statistics
json
"""

"""
=========================================================
12. math MODULE
=========================================================
"""

import math

print(math.pi)
print(math.floor(34))
print(math.ceil(36))
print(math.exp(5))

"""
output:

3.141592653589793
34
36
148.4131591025766
"""

"""
=========================================================
13. random MODULE
=========================================================
"""

import random

print(random.randint(1,100))
print(random.betavariate(20,100))

fruits = ["apple", "banana", "mango","cherry","papaya","grape","orange","guava"]
print(random.choice(fruits))
print(random.choices(fruits))

"""
Output:

Random number between 1 and 100

Random fruit from list
"""

"""
=========================================================
14. datetime MODULE
=========================================================
"""

import datetime

today = datetime.date.today()
print(today)

"""
Output:

Current date
"""

"""
=========================================================
15. os MODULE
=========================================================
"""
import os

print(os.getcwd())

"""
getcwd()

Means:

Get Current Working Directory
"""

"""
=========================================================
16. sys MODULE
=========================================================
"""

import sys

print(sys.version)


"""
Shows current Python version.
"""


"""
=========================================================
17. platform MODULE
=========================================================
"""

import platform

print(platform.system())


"""
Shows operating system name.
"""

"""
=========================================================
18. statistics MODULE
=========================================================
"""

import statistics

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,1]

print(statistics.mean(numbers))
print(statistics.median(numbers))
print(statistics.mode(numbers))

"""
output:

3.769230769230769
3
1
"""

"""
=========================================================
19. json MODULE
=========================================================
"""

import json

data = '{"name":"Radha","age":21,"city":"My Heart❤️"}'

result = json.loads(data)
print(result)
print(type(result))

"""
Output:

{"name":"Radha","age":21,"city":"My Heart❤️"}

<class 'dict'>
"""

"""
=========================================================
20. dir() FUNCTION
=========================================================
"""

import math

print(dir(math))


"""
Shows all available functions inside module.
"""

"""
=========================================================
21. help() FUNCTION
=========================================================
"""

help(math.sqrt)


"""
Shows documentation for function/module.
"""

"""
=========================================================
22. __name__ VARIABLE
=========================================================
"""

print(__name__)


"""
If file runs directly:

__main__

If imported:

module name
"""

"""
=========================================================
23. MAIN GUARD
=========================================================
"""

def greet():

    print("Hello")


if __name__ == "__main__":

    greet()


"""
Prevents automatic execution during import.

Very important in professional projects.
"""

"""
=========================================================
24. HOW IMPORT ACTUALLY WORKS
=========================================================

When Python imports a module:

1. Finds the module
2. Compiles module
3. Executes module once
4. Stores module in memory
5. Reuses later imports

Python caches imported modules for efficiency.
"""

"""
=========================================================
25. MODULE SEARCH PATH
=========================================================
"""

import sys

print(sys.path)

"""
Python searches modules in:

1. Current directory
2. Installed libraries
3. System paths
"""


"""
=========================================================
26. RELOADING MODULES
=========================================================
"""

import importlib

import math

importlib.reload(math)


"""
Useful during development.
"""
