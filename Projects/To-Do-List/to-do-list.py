# TO DO LIST

tasks = []
completed_tasks = []


def menu():
    print("""
    1. Add Task
    2. Delete Task
    3. Show Tasks
    4. Modify Task
    5. Exit
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


def modify(task, new_task):
    if not tasks:
        print("Tasks list is empty.")
        return

    if not new_task:
        print("New task cannot be empty.")
        return

    if task in tasks:
        index = tasks.index(task)
        tasks[index] = new_task
        print("Task modified successfully.")
    else:
        print("Task not found.")


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
        task = input("Enter task to modify: ").strip()
        new_task = input("Enter new task name: ").strip()
        modify(task, new_task)

    elif choice == "5":
        print("Thanks for using my to-do list.")
        break

    else:
        print("Invalid choice. Please try again.")