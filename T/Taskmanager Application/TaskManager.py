# TaskManager - A Simple Task Management Application

# Dictionary to store tasks
tasks = {}

# Function to add a task
def add_task(task_name):
    tasks[task_name] = False  # Initially, tasks are marked as incomplete

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Task List:")
        for task_name, is_completed in tasks.items():
            status = "Completed" if is_completed else "Incomplete"
            print(f"- {task_name} ({status})")

# Function to mark a task as completed
def mark_as_completed(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"'{task_name}' has been marked as completed.")
    else:
        print(f"'{task_name}' is not found in the task list.")

# Function to delete a task
def delete_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"'{task_name}' has been deleted from the task list.")
    else:
        print(f"'{task_name}' is not found in the task list.")

# Main function
def main():
    while True:
        print("\n--- TaskManager ---")
        print("1. Add a Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete a Task")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
            print(f"'{task_name}' has been added to the task list.")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_name = input("Enter the task name you want to mark as completed: ")
            mark_as_completed(task_name)
        elif choice == "4":
            task_name = input("Enter the task name you want to delete: ")
            delete_task(task_name)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
