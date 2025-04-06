from file_handler import read_tasks, write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("✅ Task added successfully.")

def remove_task(task_number):
    tasks = read_tasks()
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            write_tasks(tasks)
            print(f"🗑️ Task '{removed}' removed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid integer.")

def update_task(task_number, new_task):
    tasks = read_tasks()
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            old = tasks[task_number - 1]
            tasks[task_number - 1] = new_task
            write_tasks(tasks)
            print(f"🔁 Task '{old}' updated to '{new_task}'.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid integer.")

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks available.")
    else:
        print("\n📋 Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
