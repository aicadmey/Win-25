
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for index, (task, completed) in enumerate(tasks.items(), 1):
            status = "✔" if completed else "✘"
            print(f"{index}. {task} [{status}]")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task in tasks:
        print("Task already exists in the to-do list!")
    else:
        tasks[task] = False
        print(f"Task '{task}' added to the list.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        task_name = list(tasks.keys())[task_num - 1]
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        task_name = list(tasks.keys())[task_num - 1]
        del tasks[task_name]
        print(f"Task '{task_name}' deleted from the list.")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    tasks = {}  # Dictionary to store tasks and their completion status
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()