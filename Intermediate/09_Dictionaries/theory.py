# Dictionary in python.
# A dictionary in Python is a collection of key-value pairs. It is defined using curly braces {} and each key is separated from its value by a colon (:). Dictionaries are mutable, meaning you can change their content after they have been created. Here are some key features of dictionaries in Python:
# 1. Unordered: The items in a dictionary do not have a defined order, and you cannot access them using indexing or slicing.
# 2. Key-Value Pairs: Each item in a dictionary is a key-value pair, where the key is a unique identifier for the value it is associated with. Keys must be immutable (like strings, numbers, or tuples), while values can be of any data type.
# 3. Mutable: You can add, remove, or change the key-value pairs in a dictionary after it has been created using methods like update(), pop(), and clear().
# 4. Dictionary Comprehension: Python provides a concise way to create dictionaries using dictionary comprehension, which allows you to generate a dictionary from an iterable in a single line of code.    


# Dictionary creation
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}  

# How many operations we can perform on dictionaries.
# We can perform various operations on dictionaries in Python, including:

# 1. Adding or Updating Key-Value Pairs: You can add new key-value pairs to a dictionary or update the value of an existing key by assigning a value to the key.
# Example of adding or updating key-value pairs in a dictionary
my_dict = {"name": "Alice", "age": 30}
# Adding a new key-value pair
my_dict["city"] = "New York"  # This will add the key "city" with the value "New York" to the dictionary, resulting in {'name': 'Alice', 'age': 30, 'city': 'New York'}.
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Updating the value of an existing key
my_dict["age"] = 31  # This will update the value of the key "age" from 30 to 31, resulting in {'name': 'Alice', 'age': 31, 'city': 'New York'}.
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}  

# 2. Removing Key-Value Pairs: You can remove key-value pairs from a dictionary using the pop() method or the del statement.
# Example of removing key-value pairs from a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Removing a key-value pair using pop() 
age = my_dict.pop("age")  # This will remove the key "age" and return its value, which is 30, resulting in {'name': 'Alice', 'city': 'New York'}.
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}
print(age)  # Output: 30
# Removing a key-value pair using del
del my_dict["city"]  # This will remove the key "city" and its associated value from the dictionary, resulting in {'name': 'Alice'}.
print(my_dict)  # Output: {'name': 'Alice'} 

# 3. Accessing Values: You can access the value associated with a specific key in a dictionary using square brackets [] or the get() method.
# Example of accessing values in a dictionary   
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Accessing value using square brackets
name = my_dict["name"]  # This will return the value associated with the key "name", which is "Alice".
print(name)  # Output: Alice
# Accessing value using get() method
age = my_dict.get("age")  # This will return the value associated with the key "age", which is 30. If the key does not exist, it will return None.
print(age)  # Output: 30

# 4. Dictionary Comprehension: You can create a new dictionary using dictionary comprehension, which allows you to generate a dictionary from an iterable in a single line of code.
# Example of dictionary comprehension   
squares = {x: x**2 for x in range(1, 6)}  # This will create a dictionary where the keys are numbers from 1 to 5 and the values are their squares, resulting in {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 5. Other Dictionary Methods: Python provides various built-in methods for dictionaries, such as keys(), values(), items(), update(), clear(), etc., which allow you to perform different operations on dictionaries easily.
# Example of using other dictionary methods 
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Getting all keys in the dictionary
keys = my_dict.keys()  # This will return a view object containing all the keys in the dictionary, which is dict_keys(['name', 'age', 'city']).
print(keys)  # Output: dict_keys(['name', 'age', 'city'])   
# Getting all values in the dictionary
values = my_dict.values()  # This will return a view object containing all the values in the dictionary, which is dict_values(['Alice', 30, 'New York']).
print(values)  # Output: dict_values(['Alice', 30, 'New York'])
# Getting all key-value pairs in the dictionary
items = my_dict.items()  # This will return a view object containing all the key-value pairs in the dictionary as tuples, which is dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]).
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
# Updating a dictionary with another dictionary
my_dict.update({"age": 31, "country": "USA"})  # This will update the value of the key "age" to 31 and add a new key "country" with the value "USA", resulting in {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}.
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
# Clearing all key-value pairs from a dictionary
my_dict.clear()  # This will remove all key-value pairs from the dictionary, resulting in an empty dictionary {}.
print(my_dict)  # Output: {}    


# 6. Nested Dictionaries: You can have dictionaries within dictionaries, which allows you to create more complex data structures.
# Example of nested dictionaries
person = { "name": "Alice", "age": 30, "address": {"street": "123 Main St", "city": "New York", "country": "USA"}}  # This is a dictionary that contains another dictionary as the value of the key "address".
print(person)  # Output: {'name': 'Alice', 'age': 30, 'address': {'street': '123 Main St', 'city': 'New York', 'country': 'USA'}}
# Accessing nested dictionary values
street = person["address"]["street"]  # This will access the value of the key "street" in the nested dictionary under the key "address", which is "123 Main St".
print(street)  # Output: 123 Main St
city = person["address"]["city"]  # This will access the value of the key "city" in the nested dictionary under the key "address", which is "New York".
print(city)  # Output: New York


# 7. Dictionary Views: The keys(), values(), and items() methods return view objects that provide a dynamic view of the dictionary's contents, meaning that if the dictionary is modified, the view will reflect those changes.
# Example of dictionary views
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
keys_view = my_dict.keys()  # This will return a view object containing all the keys
print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])
values_view = my_dict.values()  # This will return a view object containing all the values  
print(values_view)  # Output: dict_values(['Alice', 30, 'New York'])
items_view = my_dict.items()  # This will return a view object containing all the key-value pairs as tuples
print(items_view)  # Output: dict_items([('name', 'Alice'), ('age   ', 30), ('city', 'New York')])
# Modifying the dictionary  
my_dict["age"] = 31  # This will update the value of the key "age" to 31
print(keys_view)  # Output: dict_keys(['name', 'age', 'city'])  
print(values_view)  # Output: dict_values(['Alice', 31, 'New York'])
print(items_view)  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])


# 8. Dictionary Comprehension: You can create a new dictionary using dictionary comprehension, which allows you to generate a dictionary from an iterable in a single line of code.
# Example of dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}  # This will create a dictionary where the keys are numbers from 1 to 5 and the values are their squares, resulting in {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  


# 9. Checking for Key Existence: You can check if a specific key exists in a dictionary using the in keyword.
# Example of checking for key existence in a dictionary 
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("name" in my_dict)  # Output: True (checks if the key "name" exists in the dictionary)
print("country" in my_dict)  # Output: False (checks if the key "country" exists in the dictionary)


# 10. Iterating Over a Dictionary: You can iterate over the keys, values, or key-value pairs of a dictionary using loops.
# Example of iterating over a dictionary    
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Iterating over keys   
for key in my_dict:
    print(key)  # This will print each key in the dictionary one by one.
# Iterating over values
for value in my_dict.values():
    print(value)  # This will print each value in the dictionary one by one.
# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")  # This will print each key and its associated value in the dictionary one by one. 


# 11. Copying a Dictionary: You can create a copy of a dictionary using the copy() method or the dict() constructor.
# Example of copying a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Copying a dictionary using copy() method  
copied_dict = my_dict.copy()  # This will create a shallow copy of the dictionary, resulting in a new dictionary with the same key-value pairs as my_dict.
print(copied_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Copying a dictionary using dict() constructor
another_copied_dict = dict(my_dict)  # This will also create a shallow copy of the dictionary, resulting in a new dictionary with the same key-value pairs as my_dict.
print(another_copied_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# 12. Merging Dictionaries: You can merge two dictionaries using the update() method or the {**dict1, **dict2} syntax.
# Example of merging dictionaries   
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "country": "USA"}  
# Merging dictionaries using update() method
dict1.update(dict2)  # This will add the key-value pairs from dict2 to dict1, resulting in {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}.
print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
# Merging dictionaries using {**dict1, **dict2} syntax  
merged_dict = {**dict1, **dict2}  # This will create a new dictionary that combines the key-value pairs from both dict1 and dict2, resulting in {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}.
print(merged_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

