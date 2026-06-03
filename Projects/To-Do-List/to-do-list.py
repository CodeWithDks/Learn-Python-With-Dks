# TO DO LIST.


tasks = []


def menu():
    print("""
    1. Add Task
    2. Delete Task
    3. Show Tasks
    4. Exit
    """)


def add_task(task):
    if not task:
        print("Task cannot be empty.")
        return

    if task in tasks:
        print("This task already exists.")
    else:
        tasks.append(task)
        print("Task added successfully.")


def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'"{task}" deleted successfully.')
    else:
        print("This task does not exist.")


while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter task name: ").strip()
        add_task(task)

    elif choice == "2":
        task = input("Which task do you want to delete? ").strip()
        delete_task(task)

    elif choice == "3":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Thanks for using my to-do list.")
        break

    else:
        print("Invalid choice. Please try again.")