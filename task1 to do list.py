# To-do list program
# Create a list to store tasks
tasks = []

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} (Status: {task['status']})")

def add_task():
    task = input("Enter a task: ")
    tasks.append({'task': task, 'status': 'Pending'})
    print("Task added!")

def delete_task():
    task_number = int(input("Enter the task number to delete: "))
    try:
        del tasks[task_number - 1]
        print("Task deleted!")
    except IndexError:
        print("Task not found!")

def mark_task_as_done():
    task_number = int(input("Enter the task number to mark as done: "))
    try:
        task = tasks[task_number - 1]
        tasks[task_number - 1] = {'task': task['task'], 'status': 'Done'}
        print("Task marked as done!")
    except IndexError:
        print("Task not found!")

def mark_task_as_pending():
    task_number = int(input("Enter the task number to mark as pending: "))
    try:
        task = tasks[task_number - 1]
        tasks[task_number - 1] = {'task': task['task'], 'status': 'Pending'}
        print("Task marked as pending!")
    except IndexError:
        print("Task not found!")

while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as done")
    print("5. Mark task as pending")
    print("6. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_task_as_done()
    elif choice == "5":
        mark_task_as_pending()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose a valid option.")