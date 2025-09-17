
tasks = []

def show_menu():
    print("\n=== To-Do List App ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"✅ '{task}' has been added.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"❌ '{removed}' has been removed.")
        except (ValueError, IndexError):
            print("⚠ Invalid task number!")


while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("\nGoodbye! 👋")
        break
    else:
        print("⚠ Invalid choice! Please try again.")
