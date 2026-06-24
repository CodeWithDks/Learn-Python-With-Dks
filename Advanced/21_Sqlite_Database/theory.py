# ==========================================================
# DAY 21 - SQLITE DATABASE
# ==========================================================

# ==========================================================
# 1. WHAT IS A DATABASE?
# ==========================================================

"""
A Database is a collection of organized data.

Examples:

Student Records
Employee Records
Bank Accounts
Hospital Records
Library Records

Instead of storing data in variables,
we store data permanently in databases.
"""

# ==========================================================
# 2. WHAT IS SQLITE?
# ==========================================================

"""
SQLite is a lightweight database
built into Python.

Advantages:

✓ No installation required
✓ Fast
✓ Lightweight
✓ Easy to Learn
✓ Good for Small & Medium Projects
"""

# ==========================================================
# 3. IMPORT SQLITE3 MODULE
# ==========================================================

import sqlite3

print("SQLite Imported Successfully")


# ==========================================================
# 4. CREATE DATABASE
# ==========================================================

"""
If database does not exist,
SQLite automatically creates it.
"""

connection = sqlite3.connect("school.db")

print("Database Created")


# ==========================================================
# 5. CLOSE DATABASE CONNECTION
# ==========================================================

connection.close()

print("Connection Closed")


# ==========================================================
# 6. CREATE CURSOR OBJECT
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

print("Cursor Created")


# ==========================================================
# 7. WHAT IS CURSOR?
# ==========================================================

"""
Cursor is used to execute SQL queries.

Think of Cursor as a messenger
between Python and Database.
"""


# ==========================================================
# 8. CREATE TABLE
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

connection.commit()

print("Table Created")

connection.close()


# ==========================================================
# 9. SQLITE DATA TYPES
# ==========================================================

"""
SQLite Data Types

INTEGER
REAL
TEXT
BLOB
NULL
"""

# ==========================================================
# 10. INSERT DATA
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
INSERT INTO students(name, age, course)
VALUES('Deepak', 21, 'Python')
""")

connection.commit()

print("Record Inserted")

connection.close()


# ==========================================================
# 11. INSERT MULTIPLE RECORDS
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

students = [
    ("Rahul", 22, "Java"),
    ("Amit", 20, "Python"),
    ("Rohan", 23, "C++")
]

cursor.executemany("""
INSERT INTO students(name, age, course)
VALUES(?, ?, ?)
""", students)

connection.commit()

print("Multiple Records Inserted")

connection.close()


# ==========================================================
# 12. SELECT ALL RECORDS
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print(records)

connection.close()


# ==========================================================
# 13. LOOP THROUGH RECORDS
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for record in records:
    print(record)

connection.close()


# ==========================================================
# 14. FETCH ONE RECORD
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

record = cursor.fetchone()

print(record)

connection.close()


# ==========================================================
# 15. FETCH MANY RECORDS
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchmany(2)

print(records)

connection.close()


# ==========================================================
# 16. WHERE CLAUSE
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM students
WHERE course='Python'
""")

records = cursor.fetchall()

print(records)

connection.close()


# ==========================================================
# 17. ORDER BY
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY age
""")

records = cursor.fetchall()

print(records)

connection.close()


# ==========================================================
# 18. ORDER BY DESC
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM students
ORDER BY age DESC
""")

records = cursor.fetchall()

print(records)

connection.close()


# ==========================================================
# 19. LIMIT
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
SELECT * FROM students
LIMIT 2
""")

records = cursor.fetchall()

print(records)

connection.close()


# ==========================================================
# 20. UPDATE RECORD
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
UPDATE students
SET course='Django'
WHERE name='Deepak'
""")

connection.commit()

print("Record Updated")

connection.close()


# ==========================================================
# 21. DELETE RECORD
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
DELETE FROM students
WHERE name='Rahul'
""")

connection.commit()

print("Record Deleted")

connection.close()


# ==========================================================
# 22. COUNT RECORDS
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""
SELECT COUNT(*) FROM students
""")

count = cursor.fetchone()

print(count)

connection.close()


# ==========================================================
# 23. SEARCH STUDENT
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

student_name = "Amit"

cursor.execute("""
SELECT * FROM students
WHERE name=?
""", (student_name,))

record = cursor.fetchone()

print(record)

connection.close()


# ==========================================================
# 24. WHY USE ? PLACEHOLDER?
# ==========================================================

"""
Wrong Way:

cursor.execute(
f"SELECT * FROM students WHERE name='{name}'"
)

Can cause SQL Injection.

Correct Way:

cursor.execute(
"SELECT * FROM students WHERE name=?",
(name,)
)
"""

# ==========================================================
# 25. COMMIT()
# ==========================================================

"""
commit() permanently saves changes.

Required after:

INSERT
UPDATE
DELETE
"""

# ==========================================================
# 26. ROLLBACK()
# ==========================================================

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

try:

    cursor.execute("""
    INSERT INTO students(name, age, course)
    VALUES('Test', 20, 'Python')
    """)

    raise Exception("Something Went Wrong")

    connection.commit()

except Exception as error:

    print(error)

    connection.rollback()

connection.close()


# ==========================================================
# 27. DROP TABLE
# ==========================================================

"""
Deletes entire table.

BE CAREFUL.
"""

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

# cursor.execute("DROP TABLE students")

connection.commit()

connection.close()


# ==========================================================
# 28. CRUD OPERATIONS
# ==========================================================

"""
CRUD

C = Create
R = Read
U = Update
D = Delete

These are the most important
database operations.
"""

# ==========================================================
# 29. MINI PROJECT - ADD STUDENT
# ==========================================================

import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")

cursor.execute("""
INSERT INTO students(name, age, course)
VALUES(?, ?, ?)
""", (name, age, course))

connection.commit()

print("Student Added Successfully")

connection.close()


# ==========================================================
# 30. MINI PROJECT - VIEW STUDENTS
# ==========================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()


# ==========================================================
# 31. MINI PROJECT - UPDATE STUDENT
# ==========================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID: "))

new_course = input("Enter New Course: ")

cursor.execute("""
UPDATE students
SET course=?
WHERE id=?
""", (new_course, student_id))

connection.commit()

print("Student Updated")

connection.close()


# ==========================================================
# 32. MINI PROJECT - DELETE STUDENT
# ==========================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

student_id = int(input("Enter Student ID: "))

cursor.execute("""
DELETE FROM students
WHERE id=?
""", (student_id,))

connection.commit()

print("Student Deleted")

connection.close()


# ==========================================================
# 33. COMPLETE CRUD EXAMPLE
# ==========================================================

"""
Student Management System

Features:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student

SQLite is commonly used
for such applications.
"""

# ==========================================================
# REAL WORLD APPLICATIONS
# ==========================================================

"""
SQLite is used in:

1. Mobile Apps

2. Desktop Applications

3. Browser Storage

4. Student Management Systems

5. Inventory Systems

6. Library Management Systems

7. Small Business Software
"""

# ==========================================================
# ADVANTAGES OF SQLITE
# ==========================================================

"""
1. Built Into Python

2. No Installation Needed

3. Fast

4. Lightweight

5. Easy To Learn

6. Suitable For Beginners

7. Perfect For Projects
"""

# ==========================================================
# QUICK REVISION
# ==========================================================

"""
sqlite3
-------
Python module for SQLite

connect()
---------
Connect to database

cursor()
--------
Create cursor object

execute()
---------
Execute SQL query

commit()
--------
Save changes permanently

rollback()
----------
Undo changes

fetchone()
----------
Fetch one record

fetchmany()
-----------
Fetch multiple records

fetchall()
----------
Fetch all records

CRUD
----
Create
Read
Update
Delete

SQL Commands
------------
CREATE TABLE

INSERT INTO

SELECT

UPDATE

DELETE

DROP TABLE
"""