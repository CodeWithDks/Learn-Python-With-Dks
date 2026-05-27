# Day 6, i have learned about lists in python. Lists are a collection of items that are ordered and changeable. They are defined using square brackets [] and can contain elements of different data types, including other lists. Here are some key features of lists in Python:
# 1. Ordered: The items in a list have a defined order, and that order will not change unless you explicitly modify the list.
# 2. Changeable: You can modify a list after it has been created, such as adding, removing, or changing elements.
# 3. Allow Duplicates: A list can contain duplicate items, meaning you can have multiple occurrences of the same value in a list.
# 4. Heterogeneous: A list can contain items of different data types, such as integers, strings, floats, and even other lists.
# 5. Indexing and Slicing: You can access individual elements of a list using indexing, and you can also access a range of elements using slicing.
# 6. Built-in Methods: Python provides a variety of built-in methods for lists, such as append(), extend(), insert(), remove(), pop(), sort(), reverse(), etc., which allow you to perform various operations on lists easily.



# list creation
my_list = [1, "Hello", 3.14, [2, 4, 6]] #This is a list that contains an integer, a string, a float, and another list as its elements.
print(my_list) #Output: [1, 'Hello', 3.14, [2, 4, 6]]

# How many operations we can perform on lists.
# We can perform various operations on lists in Python, including:


# 1. Adding Elements: You can add elements to a list using methods like append(), extend(), and insert().
# Example of adding elements to a list
my_list = [1, 2, 3]
my_list.append(4)  # This will add the element 4 to the end of the list, resulting in [1, 2, 3, 4].
print(my_list)  # Output: [1, 2, 3, 4]
my_list.extend([5, 6])  # This will add the elements 5 and 6 to the end of the list, resulting in [1, 2, 3, 4, 5, 6].
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)  # This will insert the element 0 at index 0, resulting in [0, 1, 2, 3, 4, 5, 6].
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6]



# 2. Removing Elements: You can remove elements from a list using methods like remove(), pop(), and clear().
# Example of removing elements from a list
my_list = [0, 1, 2, 3, 4, 5, 6]
my_list.remove(3)  # This will remove the first occurrence of the element 3 from the list, resulting in [0, 1, 2, 4, 5, 6].
print(my_list)  # Output: [0, 1, 2, 4, 5, 6]
popped_element = my_list.pop()  # This will remove and return the last element of the list, which is 6, resulting in [0, 1, 2, 4, 5].
print(my_list)  # Output: [0, 1, 2, 4, 5]
print(popped_element)  # Output: 6
my_list.clear()  # This will remove all elements from the list, resulting in an empty list [].
print(my_list)  # Output: []



# 3. Accessing Elements: You can access individual elements of a list using indexing and slicing.
# Example of accessing elements in a list
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output: 10 (first element)
print(my_list[2])  # Output: 30 (third element)
print(my_list[-1])  # Output: 50 (last element)
print(my_list[1:4])  # Output: [20, 30, 40] (elements from index 1 to 3)



# 4. Modifying Elements: You can change the value of an element in a list by assigning a new value to a specific index.
# Example of modifying elements in a list
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25  # This will change the element at index 1 from 20 to 25, resulting in [10, 25, 30, 40, 50].
print(my_list)  # Output: [10, 25, 30, 40, 50]  



# 5. Sorting: You can sort the elements of a list using the sort() method or the sorted() function.
# Example of sorting a list
my_list = [40, 10, 30, 20, 50]  
my_list.sort()  # This will sort the list in place, resulting in [10, 20, 30, 40, 50].
print(my_list)  # Output: [10, 20, 30, 40, 50]
my_list = [40, 10, 30, 20, 50]
sorted_list = sorted(my_list)  # This will return a new sorted list, resulting in [10, 20, 30, 40, 50], while my_list remains unchanged.
print(sorted_list)  # Output: [10, 20, 30, 40, 50]
print(my_list)  # Output: [40, 10, 30, 20, 50] (original list remains unchanged)



# 6. Reversing: You can reverse the order of elements in a list using the reverse() method or slicing.
# Example of reversing a list
my_list = [10, 20, 30, 40, 50]
my_list.reverse()  # This will reverse the list in place, resulting in [50, 40, 30, 20, 10].
print(my_list)  # Output: [50, 40, 30, 20, 10]
my_list = [10, 20, 30, 40, 50]
reversed_list = my_list[::-1]  # This will return a new reversed list, resulting in [50, 40, 30, 20, 10], while my_list remains unchanged.
print(reversed_list)  # Output: [50, 40, 30, 20, 10]
print(my_list)  # Output: [10, 20, 30, 40, 50] (original list remains unchanged)



# 7. Length: You can find the number of elements in a list using the len() function.
# Example of finding the length of a list
my_list = [10, 20, 30, 40, 50]  
print(len(my_list))  # Output: 5 (number of elements in the list)   





# 8. Concatenation: You can concatenate two or more lists using the + operator.
# Example of concatenating lists
list1 = [1, 2, 3]   
list2 = [4, 5, 6]
concatenated_list = list1 + list2  # This will create a new list that combines the elements of list1 and list2, resulting in [1, 2, 3, 4, 5, 6].
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]




# 9. Repetition: You can repeat a list multiple times using the * operator. 
# Example of repeating a list
my_list = [1, 2, 3]
repeated_list = my_list * 3  # This will create a new list that repeats the elements of my_list three times, resulting in [1, 2, 3, 1, 2, 3, 1, 2, 3].
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]




# 10. Membership Testing: You can check if an element exists in a list using the in keyword.
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
