tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

def update_task():
    show_tasks()
    if not tasks:
        return

    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number - 1] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
