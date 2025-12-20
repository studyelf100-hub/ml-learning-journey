# Make a simple score tracker

# My tracker will:

# 1. Let the user add items

# 2. Store them in memory

# 3. Display all items

# Simple Task Tracker

tasks = []

print("Simple Task Tracker")

while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Clear all tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ").strip().lower()

        if task in tasks:
            print("Error: Task already exists.")
        else:
            tasks.append(task)
            print(f'Task "{task}" added.')

    elif choice == "2":
        if tasks:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks added yet.")

    elif choice == "3":
        tasks.clear()
        print("All tasks cleared.")

    elif choice == "4":
        print("Exiting the tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
