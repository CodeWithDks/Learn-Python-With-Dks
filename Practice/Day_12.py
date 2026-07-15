"""
Create a dictionary of 5 countries and their capitals. 
Loop through it and print each as: "The capital of France is Paris". 
Then ask the user to enter a country name and print its capital — 
if the country isn't in the dictionary, 
print "Country not found"."""


countries = {
    'India': 'New Delhi',
    'United States': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'Australia': 'Canberra',
    'Japan': 'Tokyo'
}

for country, capital in countries.items():
    print(f'The capital of {country} is {capital}')
    
user_input = input("Enter a country name: ").title().strip()

if user_input in countries:
    print(f"The capital of {user_input} is {countries[user_input]}")
else:
    print("Country not found")


"""
Create a nested dictionary of 3 students. 
Each student should have name, age, and marks as keys. 
Loop through it and print each student's details. 
Then print only the student with the highest marks."""

student = {
    'student1': {
        'name': 'Radha',
        'age': 21,
        'marks': 99
    },

    'student2': {
        'name': 'Ram',
        'age': 22,
        'marks': 99.9
    },

    'student3': {
        'name': 'Deepak',
        'age': 20,
        'marks': 98
    }
}

# Print all students
for student_id, info in student.items():
    print(f"{student_id}")
    print(f"Name : {info['name']}")
    print(f"Age  : {info['age']}")
    print(f"Marks: {info['marks']}\n")

# Find highest marks
highest = max(info['marks'] for info in student.values())

# Print student with highest marks
for info in student.values():
    if info['marks'] == highest:
        print("Student with highest marks:")
        print(f"Name : {info['name']}")
        print(f"Age  : {info['age']}")
        print(f"Marks: {info['marks']}")