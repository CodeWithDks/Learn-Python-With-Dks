"""
=========================================================
PYTHON LIBRARIES - COMPLETE THEORY
=========================================================
"""

"""
=========================================================
1. WHAT IS A LIBRARY?
=========================================================

A library is a collection of pre-written code that helps
developers perform tasks without writing everything
from scratch.

Libraries save:

1. Time
2. Effort
3. Development cost

Examples:

math
random
datetime
numpy
pandas
requests
django
"""

"""
=========================================================
2. WHY LIBRARIES ARE IMPORTANT
=========================================================

Imagine building:

- Calculator
- Web Application
- Data Analysis Tool
- API Client

Without libraries:

You would need to write thousands of lines of code.

Libraries provide ready-made solutions.
"""

"""
=========================================================
3. TYPES OF LIBRARIES
=========================================================

1. Standard Library
   Comes with Python

2. Third-Party Library
   Installed separately using pip
"""

"""
=========================================================
4. STANDARD LIBRARY
=========================================================

Python provides many built-in libraries.

Examples:

math
random
datetime
os
sys
json
statistics
pathlib
collections

No installation required.
"""

"""
=========================================================
5. THIRD-PARTY LIBRARIES
=========================================================

Libraries created by the Python community.

Examples:

numpy
pandas
requests
matplotlib
flask
django
beautifulsoup4

Need installation using pip.
"""

"""
=========================================================
6. WHAT IS PIP?
=========================================================

pip = Package Installer for Python

Used for:

1. Installing libraries
2. Updating libraries
3. Removing libraries
4. Managing dependencies
"""

"""
=========================================================
7. CHECKING PIP VERSION
=========================================================
"""

# pip --version


"""
Shows installed pip version.
"""

"""
=========================================================
8. INSTALLING A LIBRARY
=========================================================
"""

# pip install requests


"""
Installs requests library.
"""

"""
=========================================================
9. INSTALLING MULTIPLE LIBRARIES
=========================================================
"""

# pip install requests pandas numpy


"""
Installs multiple libraries at once.
"""

"""
=========================================================
10. UPGRADING A LIBRARY
=========================================================
"""

# pip install --upgrade requests


"""
Updates library to latest version.
"""

"""
=========================================================
11. UNINSTALLING A LIBRARY
=========================================================
"""

# pip uninstall requests


"""
Removes installed library.
"""

"""
=========================================================
12. VIEW INSTALLED LIBRARIES
=========================================================
"""

# pip list


"""
Shows all installed libraries.
"""

"""
=========================================================
13. LIBRARY INFORMATION
=========================================================
"""

# pip show requests


"""
Displays:

- version
- author
- location
- dependencies
"""

"""
=========================================================
14. math LIBRARY
=========================================================
"""

import math 
from math import sqrt, factorial, pi

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)


"""
Output:

5.0
120
3.141592653589793
"""

"""
=========================================================
15. random LIBRARY
=========================================================
"""

import random

print(random.randint(1,10))
print(random.choice(["Apple", "Banana", "Mango"]))


"""
Output:

Random values each run.
"""

"""
=========================================================
16. datetime LIBRARY
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
17. json LIBRARY
=========================================================
"""

import json

data = '{"name":"Deepak","age":22}'

result = json.loads(data)
print(result)


"""
Output:

{'name': 'Deepak', 'age': 22}
"""


"""
=========================================================
18. statistics LIBRARY
=========================================================
"""

import statistics

numbers = [10,20,30,40,50]

print(statistics.mean(numbers))
print(statistics.median(numbers))


"""
Output:

30
30
"""

"""
=========================================================
19. pathlib LIBRARY
=========================================================
"""

from pathlib import Path

path = Path("math_utils.py")
print(path.exists())

"""
Checks whether file exists.
"""

"""
=========================================================
20. collections LIBRARY
=========================================================
"""

from collections import Counter

data = ["a", "b", "a", "c", "a"]
print(Counter(data))

"""
Output:

Counter({'a': 3, 'b': 1, 'c': 1})
"""

"""
=========================================================
21. INTRODUCTION TO REQUESTS LIBRARY
=========================================================

requests is one of the most popular Python libraries.

Used for:

- API calls
- Downloading data
- Web communication
"""

"""
=========================================================
22. INSTALLING REQUESTS
=========================================================
"""

# pip install requests


"""
Installs requests library.
"""

"""
=========================================================
23. BASIC REQUEST EXAMPLE
=========================================================
"""

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)


"""
Output:

200
"""

"""
=========================================================
24. INTRODUCTION TO NUMPY
=========================================================

NumPy is used for:

- Numerical computing
- Scientific calculations
- Fast mathematical operations

Popular in:

- Data Science
- Machine Learning
- AI
"""

"""
=========================================================
25. INSTALLING NUMPY
=========================================================
"""

# pip install numpy


"""
Installs NumPy.
"""

"""
=========================================================
26. BASIC NUMPY EXAMPLE
=========================================================
"""

# import numpy as np

# arr = np.array([1,2,3,4])

# print(arr)


"""
Output:

[1 2 3 4]
"""

"""
=========================================================
27. INTRODUCTION TO PANDAS
=========================================================

Pandas is used for:

- Data Analysis
- Data Cleaning
- CSV Processing
- Excel Processing

One of the most important libraries.
"""


"""
=========================================================
28. INSTALLING PANDAS
=========================================================
"""

# pip install pandas


"""
Installs Pandas.
"""

"""
=========================================================
29. BASIC PANDAS EXAMPLE
=========================================================
"""

# import pandas as pd

# data = {
#     "Name": ["Deepak", "Rahul"],
#     "Age": [22, 21]
# }

# df = pd.DataFrame(data)

# print(df)

"""
Creates DataFrame.
"""


"""
=========================================================
30. INTRODUCTION TO MATPLOTLIB
=========================================================

Matplotlib is used for:

- Graphs
- Charts
- Data Visualization
"""

"""
=========================================================
31. INSTALLING MATPLOTLIB
=========================================================
"""

# pip install matplotlib


"""
Installs Matplotlib.
"""


"""
=========================================================
32. BASIC MATPLOTLIB EXAMPLE
=========================================================
"""

# import matplotlib.pyplot as plt

# x = [1,2,3]

# y = [10,20,30]

# plt.plot(x,y)

# plt.show()

"""
Displays line graph.
"""

"""
=========================================================
33. VIRTUAL ENVIRONMENT
=========================================================

Professional developers rarely install
libraries globally.

Instead they use virtual environments.
"""

"""
=========================================================
34. CREATING VIRTUAL ENVIRONMENT
=========================================================
"""

# python -m venv myenv


"""
Creates isolated environment.
"""

"""
=========================================================
35. ACTIVATING VIRTUAL ENVIRONMENT
=========================================================
"""

# Windows

# myenv\Scripts\activate


"""
Activates virtual environment.
"""

"""
=========================================================
36. DEACTIVATING VIRTUAL ENVIRONMENT
=========================================================
"""

# deactivate


"""
Leaves virtual environment.
"""

"""
=========================================================
37. requirements.txt
=========================================================

Stores project dependencies.

Very important in real-world projects.
"""

"""
=========================================================
38. CREATING requirements.txt
=========================================================
"""

# pip freeze > requirements.txt


"""
Saves all installed libraries.
"""

"""
=========================================================
39. INSTALLING FROM requirements.txt
=========================================================
"""

# pip install -r requirements.txt


"""
Installs all required libraries.
"""

"""
=========================================================
40. LIBRARY VS MODULE
=========================================================

Module:
Single Python file

Example:

math.py


Library:
Collection of modules/packages

Example:

NumPy
Pandas
Django
"""

"""
=========================================================
41. COMMON BEGINNER MISTAKES
=========================================================

1. Installing everything globally

2. Not using virtual environments

3. Blindly copying imports

4. Installing unused libraries

5. Ignoring documentation
"""

"""
=========================================================
42. BEST PRACTICES
=========================================================

1. Read documentation

2. Install only required libraries

3. Use virtual environments

4. Keep requirements.txt updated

5. Learn one library deeply before moving to another
"""

"""
=========================================================
43. INTERVIEW QUESTIONS
=========================================================

1. What is a library?

2. Difference between library and module

3. What is pip?

4. What is virtual environment?

5. What is requirements.txt?

6. Difference between standard library and
   third-party library
"""

"""
=========================================================
44. FINAL SUMMARY
=========================================================

Libraries are one of the biggest reasons Python is so
popular.

Libraries allow developers to:

- Build applications faster
- Write less code
- Solve complex problems easily

Learning libraries is essential for:

- Web Development
- Data Science
- Machine Learning
- Automation
- Backend Development
"""

