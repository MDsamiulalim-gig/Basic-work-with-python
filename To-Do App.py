# Simple To-Do List

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid input!")

def todo_app():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

todo_app()