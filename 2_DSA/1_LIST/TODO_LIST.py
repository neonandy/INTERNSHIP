tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n---Your tasks---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"✅ '{task}' added!")

def delete_task(number):
    removed = tasks.pop(number - 1)
    print(f"✅ '{removed}' removed!")


#creating object / USAGE

add_task("4 to 6 Gym")
add_task("7 to 10 Coding")
add_task("10 to 11 Practice")
add_task("11 to 12 Social Media")
show_tasks()
delete_task(4)
show_tasks()