"""
=========================================================
PYTHON EXCEPTION HANDLING - COMPLETE THEORY
=========================================================
"""

"""
=========================================================
1. WHAT IS AN EXCEPTION?
=========================================================

An exception is an error that occurs during program execution.

When an exception occurs:

1. Program stops execution
2. Python generates an error message

Examples:

- Dividing by zero
- Accessing invalid list index
- Opening non-existing file
- Invalid type operations
"""

"""
=========================================================
2. WHY EXCEPTION HANDLING IS IMPORTANT?
=========================================================

Without exception handling:

Program crashes immediately.

With exception handling:

Program handles errors gracefully and continues running.

This improves:

1. User experience
2. Program reliability
3. Code quality
"""

"""
=========================================================
3. EXAMPLE WITHOUT EXCEPTION HANDLING
=========================================================
"""

num = 10

#print(num / 0)

"""
Output:

ZeroDivisionError

Program crashes.
"""

"""
=========================================================
4. BASIC try-except
=========================================================
"""
try:

    print(10 / 0)

except:

    print("An error occurred\n")


"""
Output:

An error occurred
"""

"""
=========================================================
5. HOW try-except WORKS
=========================================================

try:

    Code that may cause error

except:

    Runs only if error occurs
"""

"""
=========================================================
6. HANDLING SPECIFIC EXCEPTIONS
=========================================================
"""

try:

    print(10 / 0)

except ZeroDivisionError:

    print("Cannot divide by zero\n")


"""
Output:

Cannot divide by zero
"""

"""
=========================================================
7. MULTIPLE EXCEPTIONS
=========================================================
"""

try:
    num = int(input("Enter Your Number: "))
    print(num / 0)

except ValueError:
    print("Enter numeric number")

except ZeroDivisionError:
    print("Can't divide by zero.\n")
    
"""
Different exceptions handled separately.
"""

"""
=========================================================
8. EXCEPTION AS VARIABLE
=========================================================
"""

try:

    print(20 / 0)

except Exception as error:

    print(error,"\n")


"""
Output:

division by zero
"""

"""
=========================================================
9. WHAT IS Exception?
=========================================================

Exception is the parent class of most built-in errors.

Using:

except Exception as e

catches most runtime errors.
"""

"""
=========================================================
10. COMMON BUILT-IN EXCEPTIONS
=========================================================

ZeroDivisionError

ValueError

TypeError

IndexError

KeyError

FileNotFoundError

AttributeError

NameError
"""

"""
=========================================================
11. ZeroDivisionError
=========================================================
"""

try:

    print(num / 0)

except ZeroDivisionError:
    print("Division by zero is not allowed\n")


"""
Occurs when dividing by zero.
"""

"""
=========================================================
12. ValueError
=========================================================
"""

try:

    age = int("abc")

except ValueError:
    print("Invalid value\n")


"""
Occurs when invalid value is provided.
"""

"""
=========================================================
13. TypeError
=========================================================
"""
try:

    result = 10 + "20"

except TypeError:

    print("Incompatible data types")


"""
Occurs when operation uses wrong data types.
"""

"""
=========================================================
14. IndexError
=========================================================
"""
try:

    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:

    print("Index out of range\n")


"""
Occurs when invalid index is used.
"""

"""
=========================================================
15. KeyError
=========================================================
"""

try:
    student = {
        "name": "Deepak"
    }
    print(student["age"])

except KeyError:
    print("Key does not exist\n")

"""
Occurs when dictionary key is missing.
"""

"""
=========================================================
16. NameError
=========================================================
"""

try:
    print(username)

except NameError:
    print("Variable not found")


"""
Occurs when variable does not exist.
"""

"""
=========================================================
17. FileNotFoundError
=========================================================
"""

try:
    open("data.txt")

except FileNotFoundError:
    print("File not found")


"""
Occurs when file does not exist.
"""

"""
=========================================================
18. else BLOCK
=========================================================
"""

try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("Valid input")

"""
else executes only if no exception occurs.
"""

"""
=========================================================
19. finally BLOCK
=========================================================
"""

try:
    print("Program running\n")

except:
    print("Error occurred\n")

finally:
    print("Always executes\n")

"""
finally always runs.

Whether error occurs or not.
"""

"""
=========================================================
20. try-except-else-finally
=========================================================
"""

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number.")

else:
    print("Age accepted.")

finally:
    print("Program finished.")

"""
Complete exception handling structure.
"""

"""
=========================================================
21. CATCHING MULTIPLE EXCEPTIONS TOGETHER
=========================================================
"""

try:
    value = int(input())
    print(10 / value)

except (ValueError, ZeroDivisionError):
    print("Invalid operation\n")


"""
Handles multiple exceptions together.
"""

"""
=========================================================
22. GENERIC EXCEPTION HANDLER
=========================================================
"""

try:
    print(10 / 0)

except Exception as e:
    print("Error:", e)


"""
Useful when exact exception is unknown.
"""

"""
=========================================================
23. NESTED try-except
=========================================================
"""

try:

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Exception")

except:
    print("Outer Exception")


"""
Nested exception handling is possible.
"""

"""
=========================================================
24. RAISING EXCEPTIONS
=========================================================
"""

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

"""
raise manually generates exception.
"""

"""
=========================================================
25. CUSTOM ERROR MESSAGE
=========================================================
"""

salary = -1000
if salary < 0:
    raise ValueError("Salary cannot be negative")

"""
Creates meaningful error messages.
"""

"""
=========================================================
26. USER-DEFINED EXCEPTION
=========================================================
"""
class InvalidAgeError(Exception):
    pass

age = -5

if age < 0:
    raise InvalidAgeError("Invalid age entered")

"""
Custom exception created by programmer.
"""

"""
=========================================================
27. ASSERT STATEMENT
=========================================================
"""

age = 20
assert age >= 18
print("Eligible")

"""
assert checks condition.

Raises AssertionError if condition is False.
"""

"""
=========================================================
28. ASSERTION ERROR
=========================================================
"""

age = 15

# assert age >= 18

"""
Raises:

AssertionError
"""

"""
=========================================================
29. EXCEPTION HIERARCHY
=========================================================

BaseException

    Exception

        ValueError

        TypeError

        IndexError

        KeyError

        FileNotFoundError

        ZeroDivisionError
    
Most built-in exceptions inherit from Exception.
"""

"""
=========================================================
30. EXCEPTION HANDLING WITH FILES
=========================================================
"""

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

"""
Common real-world use case.
"""

"""
=========================================================
31. EXCEPTION HANDLING WITH USER INPUT
=========================================================
"""

try:

    age = int(input("Enter age: "))
    print(age)

except ValueError:
    print("Please enter numbers only")

"""
Prevents program crashes from invalid input.
"""

"""
=========================================================
32. REAL-WORLD LOGIN EXAMPLE
=========================================================
"""

try:
    username = input("Username: ")

    if username == "":
        raise ValueError("Username cannot be empty")

except ValueError as e:
    print(e)


"""
Validates user input.
"""

"""
=========================================================
33. COMMON BEGINNER MISTAKES
=========================================================

1. Using bare except everywhere

2. Ignoring error messages

3. Catching every exception unnecessarily

4. Not using finally for cleanup

5. Writing try blocks that are too large
"""

"""
=========================================================
34. BEST PRACTICES
=========================================================

1. Catch specific exceptions

2. Use meaningful error messages

3. Keep try blocks small

4. Use finally for cleanup

5. Log errors in real applications

6. Avoid using:

   except:

   unless absolutely necessary
"""


"""
=========================================================
35. INTERVIEW QUESTIONS
=========================================================

1. What is an exception?

2. Difference between syntax error and exception?

3. Difference between error and exception?

4. What is try-except?

5. Difference between else and finally?

6. What is raise?

7. What is a custom exception?

8. Why should we avoid bare except?

9. What is AssertionError?

10. What is Exception class?
"""


"""
=========================================================
36. FINAL SUMMARY
=========================================================

Exception Handling allows programs to handle errors
gracefully without crashing.

Important concepts:

- try
- except
- else
- finally
- raise
- assert
- custom exceptions

Exception Handling is heavily used in:

- File Handling
- APIs
- Databases
- Web Development
- Automation Scripts

A professional Python developer writes code
expecting errors and handling them properly.
"""






