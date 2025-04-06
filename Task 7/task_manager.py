from task_operations import add_task, remove_task, update_task, view_tasks
from file_handler import ensure_file_exists

def display_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def main():
    ensure_file_exists()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
            task_number = input("Enter task number to remove: ")
            remove_task(task_number)
        elif choice == '3':
            view_tasks()
            task_number = input("Enter task number to update: ")
            new_task = input("Enter new task: ")
            update_task(task_number, new_task)
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
