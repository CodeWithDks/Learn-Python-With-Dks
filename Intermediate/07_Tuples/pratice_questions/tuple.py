# practice questions on tuples


# 1. Create a tuple with the following values: "apple", "banana", "cherry"
my_tuple = ("apple", "banana", "cherry")



# 2. Access the second item in the tuple and print it.
print(my_tuple[1]) # Output: banana




# 3. Try to change the value of the first item in the tuple to "grape" and observe what happens.
# my_tuple[0] = "grape" # This will raise a TypeError because tuples are immutable and do not support item assignment.


# 4. Create a new tuple by concatenating the original tuple with another tuple containing the values "grape" and "orange".
new_tuple = my_tuple + ("grape", "orange")  

# 5. Print the new tuple.
print(new_tuple) # Output: ('apple', 'banana', 'cherry', 'grape', 'orange')

# 6. Find the length of the new tuple and print it.
print(len(new_tuple)) # Output: 5 (number of elements in the new tuple)

# 7. Create a tuple with a single value "apple". Print the tuple and its type.
single_tuple = ("apple",)  # Note the comma after "apple" to indicate that this is a tuple with a single element.
print(single_tuple)  # Output: ('apple',)
print(type(single_tuple))  # Output: <class 'tuple'> (the type of single_tuple is tuple)


# Tuple use on real world applications simple questions.

# 1. Create a tuple to store the coordinates of a point in 2D space (x, y). Print the coordinates.
coordinates = (3, 4)  # This tuple represents the coordinates (x, y) of a point in 2D space.
print(coordinates)  # Output: (3, 4)    

# 2. Create a tuple to store the RGB color values (red, green, blue) for a color. Print the RGB values.
rgb_color = (255, 0, 0)  # This tuple represents the RGB color values for red, where red is 255 and green and blue are 0.
print(rgb_color)  # Output: (255, 0, 0)

# 3. Create a tuple to store the days of the week. Print the days.
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  # This tuple contains the names of the days of the week.
print(days_of_week)  # Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# 4. Create a tuple to store the names of three cities you want to visit. Print the city names.
cities_to_visit = ("Paris", "Tokyo", "New York")  # This tuple contains the names of three cities that I want to visit.
print(cities_to_visit)  # Output: ('Paris', 'Tokyo', 'New York')


# 5. Create a tuple to store the names of three programming languages you want to learn. Print the language names.
languages_to_learn = ("Python", "JavaScript", "Go")  # This tuple contains the names of three programming languages that I want to learn.
print(languages_to_learn)  # Output: ('Python', 'JavaScript', 'Go')


# 6. Create a tuple to store the names of three fruits you like. Print the fruit names.
favorite_fruits = ("Mango", "Strawberry", "Pineapple")  # This tuple contains the names of three fruits that I like.
print(favorite_fruits)  # Output: ('Mango', 'Strawberry', 'Pineapple')


# 7. Create a tuple to store the names of three sports you enjoy watching. Print the sport names.
favorite_sports = ("Football", "Basketball", "Tennis")  # This tuple contains the names of three sports that I enjoy watching.
print(favorite_sports)  # Output: ('Football', 'Basketball', 'Tennis')


# 8. Create a tuple to store the names of three movies you want to watch. Print the movie names.
movies_to_watch = ("Inception", "The Matrix", "Interstellar")  # This   tuple contains the names of three movies that I want to watch.
print(movies_to_watch)  # Output: ('Inception', 'The Matrix', ' Interstellar')


# 9. Create a tuple to store the names of three books you want to read. Print the book names.
books_to_read = ("To Kill a Mockingbird", "1984", "The Great Gatsby")  # This tuple contains the names of three books that I want to read.
print(books_to_read)  # Output: ('To Kill a Mockingbird', '1984', 'The Great Gatsby')



# 10. Create a tuple to store the names of three countries you want to visit. Print the country names.
countries_to_visit = ("Italy", "Japan", "Australia")  # This tuple contains the names of three countries that I want to visit.
print(countries_to_visit)  # Output: ('Italy', 'Japan', 'Australia')

# Some logical questions on tuples.

# 1. Why are tuples considered immutable in Python? What are the advantages of using tuples over lists?
# Tuples are considered immutable in Python because once a tuple is created, its elements cannot be changed, added, or removed. This immutability provides several advantages over lists:
# 1. Performance: Tuples are generally faster than lists because they are immutable and have a smaller memory footprint. This makes them more efficient for storing and accessing data that does not need to be modified.
# 2. Hashability: Since tuples are immutable, they can be used as keys in dictionaries and elements in sets, whereas lists cannot be used in these contexts because they are mutable.
# 3. Data Integrity: Using tuples can help ensure that the data remains unchanged throughout the    program, which can be beneficial for maintaining data integrity and preventing accidental modifications.
# 2. Can you modify the elements of a tuple after it has been created? If not, how can you achieve similar functionality using tuples?
