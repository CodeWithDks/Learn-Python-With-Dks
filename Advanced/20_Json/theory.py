# ==========================================================
# DAY 20 - JSON & APIs
# ==========================================================

# ==========================================================
# 1. WHAT IS JSON?
# ==========================================================

"""
JSON = JavaScript Object Notation

JSON is a lightweight format used to store
and exchange data.

JSON is the most common format used by APIs.

Example JSON:

{
    "name": "Deepak",
    "age": 21,
    "city": "Arrah"
}
"""

# ==========================================================
# 2. WHY JSON?
# ==========================================================

"""
JSON is:

1. Lightweight
2. Easy to Read
3. Easy to Write
4. Human Readable
5. Supported by Almost Every Language
6. Widely Used in APIs
"""

# ==========================================================
# 3. IMPORT JSON MODULE
# ==========================================================

import json

print("JSON Module Imported Successfully")


# ==========================================================
# 4. PYTHON DICTIONARY VS JSON
# ==========================================================

"""
Python Dictionary:
------------------
{
    'name': 'Deepak'
}

JSON:
-----
{
    "name": "Deepak"
}

Difference:
-----------
Dictionary uses single or double quotes.

JSON uses double quotes only.
"""

# ==========================================================
# 5. JSON DATA TYPES
# ==========================================================

"""
JSON Type       Python Type
--------------------------------
String          str
Number          int/float
Boolean         bool
Array           list
Object          dict
null            None
"""

# ==========================================================
# 6. PYTHON OBJECT
# ==========================================================

student = {
    "name": "Deepak",
    "age": 21,
    "course": "Python"
}

print(student)


# ==========================================================
# 7. json.dumps()
# ==========================================================

"""
Convert Python Object -> JSON String
"""

student = {
    "name": "Deepak",
    "age": 21
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))


# ==========================================================
# 8. json.loads()
# ==========================================================

"""
Convert JSON String -> Python Object
"""

json_string = '{"name":"Deepak","age":21}'

python_data = json.loads(json_string)

print(python_data)
print(type(python_data))


# ==========================================================
# 9. INDENTING JSON
# ==========================================================

student = {
    "name": "Deepak",
    "age": 21,
    "city": "Arrah"
}

formatted = json.dumps(student, indent=4)

print(formatted)


# ==========================================================
# 10. SORTING JSON KEYS
# ==========================================================

student = {
    "city": "Arrah",
    "name": "Deepak",
    "age": 21
}

result = json.dumps(
    student,
    indent=4,
    sort_keys=True
)

print(result)


# ==========================================================
# 11. JSON FILE WRITING
# ==========================================================

student = {
    "name": "Deepak",
    "age": 21,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created")


# ==========================================================
# 12. JSON FILE READING
# ==========================================================

with open("student.json", "r") as file:
    data = json.load(file)

print(data)


# ==========================================================
# 13. WRITING MULTIPLE RECORDS
# ==========================================================

students = [
    {
        "name": "Deepak",
        "age": 21
    },
    {
        "name": "Rahul",
        "age": 22
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Students Saved")


# ==========================================================
# 14. READING MULTIPLE RECORDS
# ==========================================================

with open("students.json", "r") as file:
    data = json.load(file)

print(data)


# ==========================================================
# 15. WHAT IS AN API?
# ==========================================================

"""
API = Application Programming Interface

API allows different software applications
to communicate with each other.

Example:

Weather App
      ↓
Weather API
      ↓
Weather Data
"""

# ==========================================================
# 16. REAL LIFE API EXAMPLES
# ==========================================================

"""
1. Weather API
2. Google Maps API
3. YouTube API
4. Facebook API
5. Instagram API
6. Payment APIs
7. Currency APIs
"""

# ==========================================================
# 17. WHY APIs?
# ==========================================================

"""
Without API:

You build everything yourself.

With API:

You use existing services and data.

Saves:
-------
✓ Time
✓ Money
✓ Effort
"""

# ==========================================================
# 18. REST API
# ==========================================================

"""
REST = Representational State Transfer

Most modern APIs are REST APIs.

Communication happens using:

HTTP Requests
and
HTTP Responses
"""

# ==========================================================
# 19. HTTP METHODS
# ==========================================================

"""
GET
POST
PUT
PATCH
DELETE
"""

# ==========================================================
# 20. GET METHOD
# ==========================================================

"""
GET

Used to fetch data from server.

Example:
Get weather data.
Get user details.
Get products.
"""

# ==========================================================
# 21. POST METHOD
# ==========================================================

"""
POST

Used to send data to server.

Example:
Register User
Create Product
Submit Form
"""

# ==========================================================
# 22. PUT METHOD
# ==========================================================

"""
PUT

Used to update entire resource.
"""

# ==========================================================
# 23. PATCH METHOD
# ==========================================================

"""
PATCH

Used to update specific fields.
"""

# ==========================================================
# 24. DELETE METHOD
# ==========================================================

"""
DELETE

Used to remove data.
"""

# ==========================================================
# 25. INSTALL REQUESTS MODULE
# ==========================================================

"""
pip install requests
"""

# ==========================================================
# 26. IMPORT REQUESTS MODULE
# ==========================================================

try:
    import requests
except ImportError:
    print("The 'requests' module is not installed. Run 'pip install requests' and try again.")
    requests = None
else:
    print("Requests Imported Successfully")


# ==========================================================
# 27. FIRST API REQUEST
# ==========================================================

"""
GET Request Example
"""

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response)


# ==========================================================
# 28. STATUS CODE
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

"""
200 = Success
404 = Not Found
500 = Server Error
"""


# ==========================================================
# 29. RESPONSE TEXT
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.text)


# ==========================================================
# 30. RESPONSE JSON
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print(data)


# ==========================================================
# 31. LOOP THROUGH API DATA
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print(user["name"])


# ==========================================================
# 32. FETCH SINGLE USER
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user = response.json()

print(user)


# ==========================================================
# 33. GET USER NAME
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user = response.json()

print(user["name"])


# ==========================================================
# 34. GET USER EMAIL
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user = response.json()

print(user["email"])


# ==========================================================
# 35. SEND DATA USING POST
# ==========================================================

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Python",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.post(
    url,
    json=new_post
)

print(response.status_code)
print(response.json())


# ==========================================================
# 36. UPDATE DATA USING PUT
# ==========================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Content",
    "userId": 1
}

response = requests.put(
    url,
    json=updated_post
)

print(response.status_code)
print(response.json())


# ==========================================================
# 37. DELETE REQUEST
# ==========================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print(response.status_code)


# ==========================================================
# 38. HANDLING API ERRORS
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(url)

    response.raise_for_status()

    print("Request Successful")

except requests.exceptions.RequestException as error:

    print("Error:", error)


# ==========================================================
# 39. REQUEST TIMEOUT
# ==========================================================

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    print(response.status_code)

except requests.exceptions.Timeout:

    print("Request Timed Out")


# ==========================================================
# 40. CUSTOM HEADERS
# ==========================================================

headers = {
    "User-Agent": "Python-App"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(response.status_code)


# ==========================================================
# 41. WEATHER API STRUCTURE
# ==========================================================

"""
Weather App
    ↓
Send Request
    ↓
Weather API
    ↓
JSON Response
    ↓
Display Weather
"""

# ==========================================================
# 42. CURRENCY API STRUCTURE
# ==========================================================

"""
Currency Converter
        ↓
Currency API
        ↓
JSON Data
        ↓
Display Result
"""

# ==========================================================
# 43. RANDOM USER API PROJECT
# ==========================================================

url = "https://randomuser.me/api"

response = requests.get(url)

data = response.json()

user = data["results"][0]

print("Name:", user["name"]["first"])
print("Email:", user["email"])


# ==========================================================
# 44. PRACTICE PROJECT - USER DIRECTORY
# ==========================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:

    print("-" * 30)

    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Phone:", user["phone"])


# ==========================================================
# 45. PRACTICE PROJECT - POSTS VIEWER
# ==========================================================

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()

for post in posts[:5]:

    print("-" * 30)

    print("Title:", post["title"])


# ==========================================================
# ADVANTAGES OF JSON
# ==========================================================

"""
1. Lightweight

2. Easy to Read

3. Easy to Parse

4. Language Independent

5. Used Everywhere
"""


# ==========================================================
# ADVANTAGES OF APIs
# ==========================================================

"""
1. Access Real Data

2. Save Development Time

3. Connect Applications

4. Automation

5. Modern Software Development
"""


# ==========================================================
# QUICK REVISION
# ==========================================================

"""
JSON
----
Data Exchange Format

json.dumps()
------------
Python -> JSON String

json.loads()
------------
JSON String -> Python

json.dump()
-----------
Python -> JSON File

json.load()
-----------
JSON File -> Python

API
---
Application Programming Interface

HTTP METHODS
------------
GET     -> Fetch Data
POST    -> Create Data
PUT     -> Update Data
PATCH   -> Partial Update
DELETE  -> Remove Data

requests.get()
--------------
Fetch Data

response.json()
---------------
Convert API Response
into Python Object

status_code
-----------
Check Request Status
"""