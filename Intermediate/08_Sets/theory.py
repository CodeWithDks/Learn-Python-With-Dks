# Sets in python.
# A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() function. Sets are mutable, meaning you can add or remove elements from them, but they do not allow duplicate values. Here are some key features of sets in Python:
# 1. Unordered: The elements in a set do not have a defined order, and you cannot access them using indexing or slicing.
# 2. Unique: A set can only contain unique elements, meaning that if you try to add a duplicate element to a set, it will be ignored.
# 3. Mutable: You can add or remove elements from a set after it has been created using methods like add(), remove(), and discard().
# 4. Set Operations: Sets support various operations like union, intersection, difference, and symmetric difference, which allow you to perform mathematical set operations on them.    


# Set creation
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# How many operations we can perform on sets.
# We can perform various operations on sets in Python, including:

# 1. Adding Elements: You can add elements to a set using the add() method.
# Example of adding elements to a set  
# Creating a set
my_set = {1, 2, 3}
# Adding an element to the set
my_set.add(4)  # This will add the element 4 to the set, resulting in {1, 2, 3, 4}.
print(my_set)  # Output: {1, 2, 3, 4}

# 2. Removing Elements: You can remove elements from a set using the remove() and discard() methods.
# Example of removing elements from a set   
# Creating a set
my_set = {1, 2, 3, 4}
# Removing an element from the set using remove()
my_set.remove(3)  # This will remove the element 3 from the set,
# resulting in {1, 2, 4}. If the element does not exist, it will raise a KeyError.
print(my_set)  # Output: {1, 2, 4}
# Removing an element from the set using discard()  
my_set.discard(2)  # This will remove the element 2 from the set, resulting in {1, 4}.
# If the element does not exist, it will not raise an error.
print(my_set)  # Output: {1, 4}

# 3. Set Operations: You can perform various set operations like union, intersection, difference, and symmetric difference.
# Example of set operations
set_a = {1, 2, 3, 4}    
set_b = {3, 4, 5, 6}    
# Union: The union of two sets contains all the elements from both sets.
union_set = set_a.union(set_b)  # This will give you {1, 2, 3, 4, 5, 6}.
print("Union:", union_set)  # Output: Union: {1, 2, 3, 4, 5, 6}
# Intersection: The intersection of two sets contains only the elements that are present in both sets.
intersection_set = set_a.intersection(set_b)  # This will give you {3, 4}.
print("Intersection:", intersection_set)  # Output: Intersection: {3, 4}
# Difference: The difference of two sets contains the elements that are present in the first set but not in the second set.
difference_set = set_a.difference(set_b)  # This will give you {1, 2}.
print("Difference:", difference_set)  # Output: Difference: {1, 2}
# Symmetric Difference: The symmetric difference of two sets contains the elements that are present in either set, but not in both sets.
symmetric_difference_set = set_a.symmetric_difference(set_b)  # This will give you {1, 2, 5, 6}.
print("Symmetric Difference:", symmetric_difference_set)  # Output: Symmetric Difference: {1, 2, 5, 6}


