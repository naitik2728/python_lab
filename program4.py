

tasks = []

while True:
    print("\n===== TASK SCHEDULER =====")
    print("1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a new task
    if choice == "1":
        name = input("Enter task name: ")

        condition = input(
            "Enter condition (ready/wait): "
        ).lower()

        # Store task as [name, condition]
        tasks.append([name, condition])

        print("Task added successfully.")

    # Run tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nChecking tasks...")

            for task in tasks:
                name = task[0]
                condition = task[1]

                # Boolean short-circuit evaluation
                if condition == "ready" and not False:
                    print("Executing:", name)

                elif condition == "wait" or condition == "ready":
                    print("Task waiting:", name)

                else:
                    print("Invalid condition:", name)

    # Display tasks
    elif choice == "3":
        if len(tasks) == 0:
            print("Task queue is empty.")
        else:
            print("\nCurrent Task Queue:")

            for i, task in enumerate(tasks, 1):
                print(i, ".", task[0], "-", task[1])

    # Exit
    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    # Invalid input
    else:
        print("Invalid choice. Please try again.")