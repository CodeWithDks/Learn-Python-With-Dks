"""Create a dictionary for a student with keys: name, age, grade, city. 
Print each value using its key. 
Then update the grade and add a new key email. 
Print the final dictionary."""

# create a dictionary
students = {
    'name' : 'Radha',
    'age' : 21,
    'grade' : 'A+',
    'city' : 'Delhi'
}

# print each values using its key.
print(f'Student name is {students['name']}.\nShe is {students["age"]} years old.\nShe is from {students["city"]}.\nshe got grade {students["grade"]}')

# update the grade
students['grade'] = 'O'

# And add new email id
students['email'] = 'radha@gmail.com'

# after updating grade and adding email id
print(f'Student name is {students['name']}.\nShe is {students["age"]} years old.\nShe is from {students["city"]}.\nshe got grade {students["grade"]}.\nAnd her email-id {students['email']}')


"""Ask the user to enter 3 students' names and their scores. 
Store them in a dictionary. 
Then print the name of the student with the highest score and the average score of all students."""

student = {}

for i in range(3):
    name = input(f'Enter student {i+1} name: ')
    score = float(input(f"Enter {name}'s score:  "))

    student[name] = score

print(student)

print(f"Highest scorer: {max(student, key=student.get)}")
print(f"Average score: {sum(student.values()) / len(student)}")
