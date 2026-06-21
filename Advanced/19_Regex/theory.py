# ==========================================================
# DAY 19 - REGULAR EXPRESSIONS (REGEX)
# ==========================================================

# ==========================================================
# 1. WHAT IS REGEX?
# ==========================================================

"""
Regex (Regular Expression) is a sequence of characters
used to search, match, validate, and manipulate text.

Examples:
---------
✓ Email Validation
✓ Password Validation
✓ Phone Number Validation
✓ Search Words
✓ Replace Text
✓ Extract Data
"""

# ==========================================================
# 2. WHY REGEX?
# ==========================================================

"""
Without Regex:
--------------
You need multiple loops and conditions.

With Regex:
-----------
Complex text operations can be done in one line.
"""

# ==========================================================
# 3. IMPORTING re MODULE
# ==========================================================

import re

print("Regex Module Imported Successfully")


# ==========================================================
# 4. re.match()
# ==========================================================

"""
re.match()

Checks pattern only at the beginning of string.
"""

text = "Python is awesome"

result = re.match("Python", text)

print(result)

if result:
    print("Match Found")
else:
    print("Match Not Found")


# ==========================================================
# 5. re.search()
# ==========================================================

"""
re.search()

Searches pattern anywhere in string.
"""

text = "I love Python Programming"

result = re.search("Python", text)

if result:
    print("Found")
else:
    print("Not Found")


# ==========================================================
# 6. re.findall()
# ==========================================================

"""
Returns all matches as a list.
"""

text = "Python Java Python C++ Python"

result = re.findall("Python", text)

print(result)


# ==========================================================
# 7. re.finditer()
# ==========================================================

"""
Returns iterator containing match objects.
"""

text = "Python Java Python"

matches = re.finditer("Python", text)

for match in matches:
    print(match.start(), match.group())


# ==========================================================
# 8. re.sub()
# ==========================================================

"""
Used to replace text.
"""

text = "I love Java"

result = re.sub("Java", "Python", text)

print(result)


# ==========================================================
# 9. re.split()
# ==========================================================

"""
Used to split string using regex pattern.
"""

text = "Apple,Banana,Mango"

result = re.split(",", text)

print(result)


# ==========================================================
# 10. REGEX METACHARACTERS
# ==========================================================

"""
Metacharacters have special meanings.

. ^ $ * + ? {} [] \ | ()
"""

# ==========================================================
# 11. DOT (.)
# ==========================================================

"""
Matches any single character except newline.
"""

text = "cat"

print(re.findall("c.t", text))


# ==========================================================
# 12. CARET (^)
# ==========================================================

"""
Checks start of string.
"""

text = "Python"

print(re.findall("^Python", text))


# ==========================================================
# 13. DOLLAR ($)
# ==========================================================

"""
Checks end of string.
"""

text = "I love Python"

print(re.findall("Python$", text))


# ==========================================================
# 14. CHARACTER CLASSES []
# ==========================================================

"""
Matches any one character inside brackets.
"""

text = "cat bat mat rat"

print(re.findall("[cbm]at", text))


# ==========================================================
# 15. RANGE IN CHARACTER CLASSES
# ==========================================================

text = "a b c d e f"

print(re.findall("[a-c]", text))


# ==========================================================
# 16. DIGITS (\d)
# ==========================================================

"""
Matches digits 0-9.
"""

text = "My age is 21"

print(re.findall(r"\d", text))


# ==========================================================
# 17. NON-DIGITS (\D)
# ==========================================================

text = "Python123"

print(re.findall(r"\D", text))


# ==========================================================
# 18. WORD CHARACTERS (\w)
# ==========================================================

"""
Letters + Digits + Underscore
"""

text = "Python_123"

print(re.findall(r"\w", text))


# ==========================================================
# 19. NON-WORD CHARACTERS (\W)
# ==========================================================

text = "Python@123"

print(re.findall(r"\W", text))


# ==========================================================
# 20. WHITESPACE (\s)
# ==========================================================

text = "Hello World"

print(re.findall(r"\s", text))


# ==========================================================
# 21. NON-WHITESPACE (\S)
# ==========================================================

text = "Hello World"

print(re.findall(r"\S", text))


# ==========================================================
# 22. QUANTIFIER *
# ==========================================================

"""
0 or more occurrences.
"""

text = "aa a aaa aaaa"

print(re.findall("a*", text))


# ==========================================================
# 23. QUANTIFIER +
# ==========================================================

"""
1 or more occurrences.
"""

text = "aa a aaa"

print(re.findall("a+", text))


# ==========================================================
# 24. QUANTIFIER ?
# ==========================================================

"""
0 or 1 occurrence.
"""

text = "color colour"

print(re.findall("colou?r", text))


# ==========================================================
# 25. QUANTIFIER {}
# ==========================================================

"""
Specify exact number of occurrences.
"""

text = "111 11 1 1111"

print(re.findall(r"\d{3}", text))


# ==========================================================
# 26. {MIN,MAX}
# ==========================================================

text = "1234 12 123456"

print(re.findall(r"\d{2,4}", text))


# ==========================================================
# 27. GROUPING ()
# ==========================================================

"""
Groups patterns together.
"""

text = "cat bat rat"

print(re.findall("(cat|bat)", text))


# ==========================================================
# 28. CAPTURING GROUPS
# ==========================================================

text = "John 25"

result = re.search(r"(\w+)\s(\d+)", text)

print(result.group(1))
print(result.group(2))


# ==========================================================
# 29. MULTIPLE CAPTURING GROUPS
# ==========================================================

text = "Deepak 21 India"

result = re.search(r"(\w+)\s(\d+)\s(\w+)", text)

print(result.groups())


# ==========================================================
# 30. NON-CAPTURING GROUP
# ==========================================================

"""
(?:pattern)
"""

text = "cat bat"

result = re.findall(r"(?:cat|bat)", text)

print(result)


# ==========================================================
# 31. EMAIL VALIDATION
# ==========================================================

email = "abc@gmail.com"

pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# ==========================================================
# 32. MOBILE NUMBER VALIDATION
# ==========================================================

mobile = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


# ==========================================================
# 33. PASSWORD VALIDATION
# ==========================================================

"""
Rules:
-------
Minimum 8 characters
At least one uppercase
At least one lowercase
At least one digit
"""

password = "Python123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")


# ==========================================================
# 34. EXTRACT ALL NUMBERS
# ==========================================================

text = "Apple 100 Mango 250 Banana 300"

numbers = re.findall(r"\d+", text)

print(numbers)


# ==========================================================
# 35. EXTRACT ALL EMAILS
# ==========================================================

text = """
abc@gmail.com
test@yahoo.com
admin@hotmail.com
"""

emails = re.findall(
    r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}",
    text
)

print(emails)


# ==========================================================
# 36. EXTRACT ALL WORDS
# ==========================================================

text = "Python is very powerful"

words = re.findall(r"\w+", text)

print(words)


# ==========================================================
# 37. REMOVE ALL DIGITS
# ==========================================================

text = "Python123Programming456"

result = re.sub(r"\d", "", text)

print(result)


# ==========================================================
# 38. REMOVE EXTRA SPACES
# ==========================================================

text = "Python     is     awesome"

result = re.sub(r"\s+", " ", text)

print(result)


# ==========================================================
# 39. CHECK IF STRING CONTAINS ONLY ALPHABETS
# ==========================================================

text = "Python"

pattern = r"^[A-Za-z]+$"

if re.match(pattern, text):
    print("Only Alphabets")
else:
    print("Contains Other Characters")


# ==========================================================
# 40. CHECK IF STRING CONTAINS ONLY NUMBERS
# ==========================================================

text = "123456"

pattern = r"^\d+$"

if re.match(pattern, text):
    print("Only Numbers")
else:
    print("Not Only Numbers")


# ==========================================================
# 41. USERNAME VALIDATION
# ==========================================================

"""
Rules:
-------
3 to 15 characters
Letters, digits, underscore only
"""

username = "deepak_123"

pattern = r"^\w{3,15}$"

if re.match(pattern, username):
    print("Valid Username")
else:
    print("Invalid Username")


# ==========================================================
# 42. DATE VALIDATION (DD-MM-YYYY)
# ==========================================================

date = "15-08-2025"

pattern = r"^\d{2}-\d{2}-\d{4}$"

if re.match(pattern, date):
    print("Valid Format")
else:
    print("Invalid Format")


# ==========================================================
# 43. URL VALIDATION
# ==========================================================

url = "https://google.com"

pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")


# ==========================================================
# 44. PRACTICE PROGRAM - FIND VOWELS
# ==========================================================

text = "Python Programming"

vowels = re.findall(r"[aeiouAEIOU]", text)

print(vowels)


# ==========================================================
# 45. PRACTICE PROGRAM - FIND WORDS STARTING WITH P
# ==========================================================

text = "Python Programming Power Practice"

result = re.findall(r"\bP\w+", text)

print(result)


# ==========================================================
# 46. PRACTICE PROGRAM - FIND ALL HASHTAGS
# ==========================================================

text = """
#python
#coding
#developer
"""

hashtags = re.findall(r"#\w+", text)

print(hashtags)


# ==========================================================
# ADVANTAGES OF REGEX
# ==========================================================

"""
1. Fast Text Searching

2. Data Validation

3. Data Extraction

4. Data Cleaning

5. Used in:
   - Web Development
   - Data Science
   - Cyber Security
   - Automation
   - Scraping
"""


# ==========================================================
# QUICK REVISION
# ==========================================================

"""
re.match()
----------
Beginning of string

re.search()
-----------
Search anywhere

re.findall()
------------
Returns list of matches

re.finditer()
-------------
Returns iterator

re.sub()
--------
Replace text

re.split()
----------
Split text

\d
--
Digit

\D
--
Non Digit

\w
--
Word Character

\W
--
Non Word Character

\s
--
Whitespace

\S
--
Non Whitespace

*
--
0 or More

+
--
1 or More

?
--
0 or 1

{}
--
Exact Count

[]
--
Character Class

()
--
Grouping

^
--
Start of String

$
--
End of String
"""