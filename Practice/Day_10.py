"""Create a tuple of 5 cities. 
Print the first and last city. 
Try to change one item — observe and write in a comment what happens and why."""

cities = ('Patna','Lukhnow','Banaras','Ilahabad','Pune')
print(cities)

# Print the first city name
print(cities[0])

# Print the last city name
print(cities[-1])

# cities.append('Delhi')
# AttributeError: 'tuple' object has no attribute 'append'

# cities[0] = 'Rachi'
# TypeError: 'tuple' object does not support item assignment

"""
Create a tuple containing a student's name, age, and grade. 
Unpack it into three separate variables and print a sentence using them. 
Then check if a specific grade exists in the tuple using the in keyword."""


# create a student with name, age and grade
student = ('Radha',21, 'A+')

# upack it into three seperate variables
name, age, grade = student

print(f'Student name is {name} and she is {age} years old and she got {grade} grade')

# check grade in student
if grade in student:
    print(grade)


