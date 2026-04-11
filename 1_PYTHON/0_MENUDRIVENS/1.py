tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task\n2. View Tasks\n3. Mark Done\n4. Delete Task\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        for i, t in enumerate(tasks, 1):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. [{status}] {t['task']}")

    elif choice == "3":
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")