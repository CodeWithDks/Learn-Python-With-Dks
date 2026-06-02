# TO DO LIST.

tasks = []

def add_task(task):
    if task not in tasks:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("This task already exists.")

while True:
    user_task = input("Enter your task name: ").strip()

    if user_task.lower() == "done":
        break

    add_task(user_task)

print("\nYour Tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")



    
