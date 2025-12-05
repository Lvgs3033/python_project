import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty! Time to add a task.")
        return
    
    print("\nCurrent To-Do List:")
    print("----------------------")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")
    print("----------------------")

def add_task(tasks):
    task = input("Enter the new task description: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'\nTask "{task}" added successfully!')
    else:
        print("\nTask description cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to remove: "))
        
        task_index = task_number - 1
        
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'\nTask "{removed_task}" removed successfully!')
        else:
            print("\nInvalid task number. Please try again.")
            
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def display_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("--------------------------")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nSaving tasks and exiting. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()