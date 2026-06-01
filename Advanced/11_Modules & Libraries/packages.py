"""
=========================================================
PYTHON PACKAGES - COMPLETE THEORY
=========================================================
"""

"""
=========================================================
1. WHAT IS A PACKAGE?
=========================================================

A package is a folder containing multiple Python modules.

Packages help organize large projects properly.

Without packages:

- projects become messy
- files become difficult to manage
- scaling becomes hard

A package usually contains:

1. Multiple modules
2. __init__.py file
"""


"""
=========================================================
2. DIFFERENCE BETWEEN MODULE AND PACKAGE
=========================================================

Module:
Single Python file

Example:

math_utils.py


Package:
Folder containing multiple modules

Example:

utilities/

    math_utils.py
    string_utils.py
"""

"""
=========================================================
3. WHY PACKAGES ARE IMPORTANT
=========================================================

Imagine a large project with:

- authentication
- database
- API handling
- payment system
- utility functions

Keeping everything in one folder becomes chaotic.

Packages organize related files together.
"""

"""
=========================================================
4. BASIC PACKAGE STRUCTURE
=========================================================
"""

# project/

#     main.py

#     utilities/

#         __init__.py
#         math_utils.py
#         string_utils.py


"""
utilities/ becomes package.

math_utils.py and string_utils.py become modules.
"""

"""
=========================================================
5. WHAT IS __init__.py ?
=========================================================

__init__.py marks a folder as a Python package.

Earlier Python versions required it strictly.

Modern Python supports namespace packages,
but __init__.py is still widely used.

It can also contain initialization code.
"""

"""
=========================================================
6. CREATING PACKAGE
=========================================================
"""

# utilities/math_utils.py

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b

"""
Now utilities folder acts as package.
"""

"""
=========================================================
7. IMPORTING MODULE FROM PACKAGE
=========================================================
"""

from utilities import math_utils

print(math_utils.add(3,5))
print(math_utils.multiplication(3,5))
print(math_utils.subtract(3,5))


"""
Output:

8
15
-2
"""

"""
=========================================================
9. IMPORTING MULTIPLE FUNCTIONS
=========================================================
"""

from utilities.math_utils import add, subtract

print(add(5,5))

print(subtract(10,5))

"""
Output:

10
5
"""

"""
=========================================================
10. PACKAGE NAMESPACE
=========================================================

utilities.math_utils.add()

Here:

utilities -> package

math_utils -> module

add -> function

Namespaces prevent naming conflicts.
"""

"""
=========================================================
11. NESTED PACKAGES
=========================================================
"""

# project/

#     app/

#         __init__.py

#         database/

#             __init__.py
#             connection.py

#         services/

#             __init__.py
#             payment.py
"""
Packages inside packages are called nested packages.
"""

"""
=========================================================
12. IMPORTING FROM NESTED PACKAGE
=========================================================
"""

# from app.database import connection


"""
=========================================================
13. ABSOLUTE IMPORT
=========================================================
"""

from utilities.math_utils import add

print(add(2,3))


"""
Uses full package path.

Recommended in most cases.
"""

"""
=========================================================
14. RELATIVE IMPORT
=========================================================
"""

# from .math_utils import add


"""
. means current package

.. means parent package

Used mostly inside packages.
"""


"""
=========================================================
15. __init__.py EXECUTION
=========================================================
"""

# utilities/__init__.py

print("Utilities package initialized")


"""
Runs automatically when package is imported.
"""

"""
=========================================================
16. USING __all__
=========================================================
"""

# utilities/__init__.py

__all__ = ["math_utils"]


"""
Controls what gets imported using:

from utilities import *
"""

"""
=========================================================
17. PACKAGE ALIASING
=========================================================
"""

import utilities.math_utils as mu

print(mu.add(5,5))


"""
Output:

10
"""

"""
=========================================================
18. dir() WITH PACKAGE
=========================================================
"""

import utilities

print(dir(utilities))


"""
Shows package attributes and methods.
"""

"""
=========================================================
19. help() WITH PACKAGE
=========================================================
"""

help(utilities)


"""
Shows package documentation.
"""

"""
=========================================================
20. PACKAGE SEARCH PATH
=========================================================
"""

import sys

print(sys.path)

"""
Python searches packages in:

1. Current directory
2. Installed libraries
3. System paths
"""

"""
=========================================================
21. IMPORTING ENTIRE PACKAGE
=========================================================
"""

import utilities


"""
Only package imports.

Modules still need explicit access.
"""

"""
=========================================================
22. PACKAGE VS LIBRARY
=========================================================

Package:
Collection of modules

Library:
Collection of packages/modules providing functionality
"""

"""
=========================================================
23. REAL-WORLD PACKAGE STRUCTURE
=========================================================
"""

# project/

#     app/

#         api/
#         models/
#         services/
#         database/
#         utils/

"""
Professional projects follow organized structure.
"""


"""
=========================================================
24. WHY PROJECT STRUCTURE MATTERS
=========================================================

Without structure:

- debugging becomes difficult
- teamwork becomes hard
- navigation becomes confusing
- scaling becomes painful
"""


"""
=========================================================
25. COMMON BEGINNER MISTAKES
=========================================================

1. Not creating __init__.py

2. Keeping everything in one folder

3. Confusing package and module

4. Using bad import structure

5. Circular imports
"""

"""
=========================================================
26. CIRCULAR IMPORT PROBLEM
=========================================================
"""

# module1 imports module2

# module2 imports module1


"""
This creates dependency loop.

Very common beginner mistake.
"""

"""
=========================================================
27. BEST PRACTICES
=========================================================

1. Use meaningful package names

2. Keep related modules together

3. Prefer absolute imports

4. Avoid circular imports

5. Keep package structure clean
"""

"""
=========================================================
28. INTERVIEW QUESTIONS
=========================================================

1. What is package?

2. Difference between module and package

3. What is __init__.py ?

4. Absolute vs relative import

5. Why packages are important?

6. What is namespace package?
"""

"""
=========================================================
29. FINAL SUMMARY
=========================================================

Packages are used to organize modules properly.

Packages are essential for:

- large projects
- scalable applications
- teamwork
- maintainable code

Without proper package structure,
real-world Python development becomes difficult.
"""