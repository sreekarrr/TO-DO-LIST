import os

FILENAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to mark as done: "))
            if 0 < num <= len(tasks):
                tasks[num-1] = tasks[num-1] + " ✅"
                save_tasks(tasks)

        elif choice == "4":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
