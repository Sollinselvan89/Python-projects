"""
Simple To-Do List Application (CLI)

Features:
- Add tasks with validation
- View numbered tasks
- Update existing tasks
- Delete tasks
- Menu-driven interaction
- Data stored in memory only

This is a basic Python CLI project that practices:
lists, loops, input validation, and CRUD operations.
"""


tasks = []


def get_user_choice():
    """Display the main menu and return the user's selected choice (1–5)."""
    print(
        "Please select the operation you want to perform\n"
        "Add task --> 1\n"
        "View tasks --> 2\n"
        "Update task --> 3\n"
        "Delete task --> 4\n"
        "Exit --> 5\n"
    )

    while True:
        choice_str = input("Please enter your choice: ")

        try:
            choice = int(choice_str)
            if not 1 <= choice <= 5:
                print("Please choose a number from 1 to 5.")
                continue
            return choice
        except ValueError:
            print("Please enter numbers only.")


def add_task():
    """Add a new task to the to-do list after validating user input."""
    while True:
        task = input("Please enter the task you want to add: ").strip()

        if not task:
            print("Task cannot be empty.")
            continue

        if not (2 <= len(task) <= 50):
            print("Task must be between 2–50 characters.")
            continue

        tasks.append(task)
        print("Task added successfully!")
        break


def view_task():
    """Display all tasks in the list with numbering."""
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def update_task():
    """Update an existing task selected by the user."""
    if not tasks:
        print("No tasks to update.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    while True:
        task_id_str = input("Please enter the task ID to update: ")

        try:
            task_id = int(task_id_str)
            if not 1 <= task_id <= len(tasks):
                print("Please choose a valid task ID.")
                continue
            break
        except ValueError:
            print("Please enter numbers only.")

    while True:
        new_task = input("Enter the new task description: ").strip()

        if not new_task:
            print("Task cannot be empty.")
            continue

        if not (2 <= len(new_task) <= 50):
            print("Task must be between 2–50 characters.")
            continue
        break

    tasks[task_id - 1] = new_task
    print("Task updated successfully!")


def delete_task():
    """Delete a task from the list based on the user-selected task ID."""
    if not tasks:
        print("No task to delete.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    while True:
        task_id_str = input("Please enter the task ID to delete: ")

        try:
            task_id = int(task_id_str)
            if not 1 <= task_id <= len(tasks):
                print("Please choose a valid task ID.")
                continue
            break
        except ValueError:
            print("Please enter numbers only.")

    removed = tasks.pop(task_id - 1)
    print(f"Task '{removed}' deleted successfully!")


def main():
    """Run the main application loop for the to-do list program."""
    print("Welcome to the Simple To-Do List App!")

    while True:
        user_choice = get_user_choice()

        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_task()
        elif user_choice == 3:
            update_task()
        elif user_choice == 4:
            delete_task()
        elif user_choice == 5:
            print("Goodbye! See you soon.")
            return


if __name__ == "__main__":
    print(">>> Program Started <<<")
    main()

