# STUDENT ADMISSION SYSTEM


class Student:

    college_name = "Noida International University"
    next_roll_no = 1

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

        # Automatically assign roll number
        self.roll_no = Student.next_roll_no
        Student.next_roll_no += 1

    def display_details(self):
        print("\n----- STUDENT DETAILS -----")
        print(f"College Name : {Student.college_name}")
        print(f"Student Name : {self.name}")
        print(f"Student Age  : {self.age}")
        print(f"Course       : {self.course}")
        print(f"Roll Number  : {self.roll_no}")



print("===== STUDENT ADMISSION SYSTEM =====")

while True:

    choice = input("\nDo you want to take admission? (yes/no): ").lower()

    if choice == "yes":

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter course name: ")

        student = Student(name, age, course)

        print("\nAdmission Successful!")
        student.display_details()

    elif choice == "no":
        print("\nThank you for visiting!")
        break

    else:
        print("\nInvalid choice. Please enter 'yes' or 'no'.")