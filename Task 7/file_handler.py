import os

TASK_FILE = "Task7/tasks.txt"

def ensure_file_exists():
    if not os.path.exists("Task7"):
        os.makedirs("Task7")
    if not os.path.isfile(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            pass

def read_tasks():
    ensure_file_exists()
    try:
        with open(TASK_FILE, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def write_tasks(tasks):
    try:
        with open(TASK_FILE, 'w') as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
