tasks = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        print("Tasks:")
        for t in tasks:
            print("-", t)

    elif choice == "3":
        break

    else:
        print("Invalid choice")