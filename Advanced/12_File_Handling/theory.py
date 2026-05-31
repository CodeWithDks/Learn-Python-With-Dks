"""
=========================================================
PYTHON FILE HANDLING - COMPLETE THEORY
=========================================================
"""
"""
=========================================================
1. WHAT IS FILE HANDLING?
=========================================================

File handling allows Python programs to:

1. Read data from files
2. Write data to files
3. Update data in files
4. Store data permanently

Without file handling, data is lost when the program ends.
"""

"""
=========================================================
2. WHY FILE HANDLING IS IMPORTANT?
=========================================================

Real-world applications use files for:

- Storing user data
- Saving logs
- Configuration files
- Reports
- CSV files
- Text documents

Examples:

Student Management System
Expense Tracker
Banking System
Inventory System
"""

"""
=========================================================
3. FILE MODES
=========================================================

r  -> Read

w  -> Write

a  -> Append

x  -> Create

r+ -> Read and Write

w+ -> Write and Read

a+ -> Append and Read

b  -> Binary Mode

t  -> Text Mode (Default)
"""
"""
=========================================================
. CREATING A FILE
=========================================================
"""

try:
    file = open("sample.txt", "x")
    print(file) 
except FileExistsError:
    print("File already exists!")

"""
=========================================================
4. OPENING A FILE
=========================================================
"""
try:
    file = open("sample.txt", "r")
    print(file)
except FileNotFoundError:
    print("File not found!")

file.close()


"""
Syntax:

open(filename, mode)

filename -> file name

mode -> operation to perform
"""

"""
=========================================================
5. READ MODE (r)
=========================================================
"""

file = open("sample.txt", "r")

print(file.read())

"""
Reads file content.
Error occurs if file does not exist.
"""

"""
=========================================================
6. WRITE MODE (w)
=========================================================
"""

file = open("sample.txt", "w")

file.write("Jay maa Radhe Rani!")
file.close

file = open("sample.txt",'r')
print(file.read())
file.close

"""
Creates file if it does not exist.
Deletes previous content if file exists.
"""

"""
=========================================================
7. APPEND MODE (a)
=========================================================
"""

file = open("sample.txt", "a")
file.write("\nRadha Rani Ji..")
file.close()

file = open("sample.txt", 'r')
print(file.read())
file.close()

"""
Adds content at the end of file.
Does not remove existing content.
"""

"""
=========================================================
8. CREATE MODE (x)
=========================================================
"""
try:
    file = open("newfile.txt", "x")
except FileExistsError:
    print("File exist already")

file = open("newfile.txt",'w')
file.write("Hello Maa Radha..")
file.close()

file = open("newfile.txt",'r')
print(file.read())
file.close()

"""
Creates file.
Raises error if file already exists.
"""

"""
=========================================================
9. CLOSE A FILE
=========================================================
"""

file = open("sample.txt", "r")
file.close()

"""
Always close files after use.
Closing file releases system resources.
"""

"""
=========================================================
10. WITH STATEMENT
=========================================================
"""

with open("sample.txt", "r") as file:

    print(file.read())

"""
Best practice.
File closes automatically.
No need to write:
file.close()
"""

"""
=========================================================
11. read()
=========================================================
"""

with open("sample.txt", "r") as file:

    content = file.read()
    print(content)

"""
Reads entire file.
"""

"""
=========================================================
12. READ SPECIFIC CHARACTERS
=========================================================
"""

with open("sample.txt", "r") as file:

    content = file.read(5)
    print(content)

"""
Reads first 5 characters.
"""

"""
=========================================================
13. readline()
=========================================================
"""
with open("sample.txt", 'r') as file:
    print(file.readline())

"""
Reads one line at a time.
"""

"""
=========================================================
14. MULTIPLE readline()
=========================================================
"""
with open("sample.txt", 'r') as file:
    print('\n')
    print(file.readline())
    print(file.readline())

"""
Reads first line then second line.
"""

"""
=========================================================
15. readlines()
=========================================================
"""
with open("sample.txt",'r') as file:
    print(file.readlines())

"""
Returns list of lines.
Example:
['Line1\\n', 'Line2\\n', 'Line3']
"""

"""
=========================================================
16. LOOP THROUGH FILE
=========================================================
"""
with open("sample.txt",'r') as file:
    for line in file:
        print(line.strip())

"""
Useful for large files.
"""

"""
=========================================================
17. write()
=========================================================
"""

with open("sample.txt", 'w') as file:
    file.write("Python\n")
    file.write("Programming..")

with open("sample.txt", 'r') as file:
    print(file.readlines())

"""
Writes content into file.
"""

"""
=========================================================
18. writelines()
=========================================================
"""

lines = [
    "Apple\n",
    "Banana\n",
    "Mango\n"
]

with open("newfile.txt", "w") as file:

    file.writelines(lines)

"""
Writes multiple lines.
"""

"""
=========================================================
19. FILE POINTER
=========================================================

Every file has a cursor (pointer).

Pointer indicates current reading position.
"""


"""
=========================================================
20. tell()
=========================================================
"""

with open("sample.txt", "r") as file:

    print(file.tell())


"""
Returns current cursor position.

Output:
0
"""

"""
=========================================================
21. seek()
=========================================================
"""

with open("sample.txt", "r") as file:

    file.seek(5)

    print(file.read())


"""
Moves cursor to specified position.
"""

"""
=========================================================
22. READ AND WRITE MODE (r+)
=========================================================
"""

with open("sample.txt", "r+") as file:

    print(file.read())

    file.write("\nMaa Radhe Rani ki Jay!")


"""
Allows reading and writing.
"""

"""
=========================================================
23. WRITE AND READ MODE (w+)
=========================================================
"""

with open("sample.txt", "w+") as file:

    file.write("I am learning python")

    file.seek(0)

    print(file.read())


"""
Previous content gets deleted.
"""

"""
=========================================================
24. APPEND AND READ MODE (a+)
=========================================================
"""

with open("sample.txt", "a+") as file:

    file.write("\nI will learn Ai")

    file.seek(0)

    print(file.read())
"""
=========================================================
25. CHECK IF FILE EXISTS
=========================================================
"""

import os

print(os.path.exists("sample.txt"))


"""
Output:

True or False
"""

