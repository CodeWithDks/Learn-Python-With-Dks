"""To-Do List App

Features:

add task
remove task
show all tasks
Skills
list methods
loops
menu systems"""

# Solution:
# Initialize an empty list to store tasks
todo_list = []
# without using functions
while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show All Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f'Task "{task}" added to the list.')
        
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print(f'Task "{task}" removed from the list.')
        else:
            print(f'Task "{task}" not found in the list.')
            
    elif choice == '3':
        if todo_list:
            print("Your To-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your To-Do List is empty.")
            
    elif choice == '4':
        print("Exiting the To-Do List App. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

