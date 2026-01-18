TASK_FILE = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print("✅ Task added successfully")

def show_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("⚠️ No tasks found")
        else:
            print("\n📋 Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

    except FileNotFoundError:
        print("⚠️ No task file found. Add a task first.")

def menu():
    while True:
        print("\n--- Task Manager CLI ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("👋 Exiting Task Manager")
            break
        else:
            print("❌ Invalid choice, try again")

# Program start
menu()