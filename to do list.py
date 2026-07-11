import json
import os
from datetime import datetime

DATABASE = "my_tasks.json"


def read_tasks():
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as file:
            return json.load(file)
    return []


def write_tasks(tasks):
    with open(DATABASE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    print("\n========== MY TASKS ==========")

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"

        print("------------------------------------")
        print("ID        :", task["id"])
        print("Task      :", task["task"])
        print("Status    :", status)
        print("Created On:", task["created"])
    print("------------------------------------")


def add_new_task(tasks):
    work = input("\nEnter new task: ")

    task = {
        "id": len(tasks) + 1,
        "task": work,
        "completed": False,
        "created": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tasks.append(task)
    write_tasks(tasks)

    print("Task added successfully.")


def edit_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter Task ID to edit: "))

        for task in tasks:
            if task["id"] == number:
                task["task"] = input("Enter new task name: ")
                write_tasks(tasks)
                print("Task updated.")
                return

        print("Task ID not found.")

    except:
        print("Invalid input.")


def complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter Task ID to complete: "))

        for task in tasks:
            if task["id"] == number:
                task["completed"] = True
                write_tasks(tasks)
                print("Congratulations! Task completed.")
                return

        print("Task ID not found.")

    except:
        print("Invalid input.")


def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    show_tasks(tasks)

    try:
        number = int(input("Enter Task ID to delete: "))

        for task in tasks:
            if task["id"] == number:
                tasks.remove(task)

                for index, t in enumerate(tasks):
                    t["id"] = index + 1

                write_tasks(tasks)

                print("Task deleted successfully.")
                return

        print("Task ID not found.")

    except:
        print("Invalid input.")


def menu():
    tasks = read_tasks()

    while True:

        print("\n")
        print("====================================")
        print("      TO-DO LIST APPLICATION")
        print("====================================")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        print("====================================")

        choice = input("Select an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_new_task(tasks)

        elif choice == "3":
            edit_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            remove_task(tasks)

        elif choice == "6":
            print("\nThank you for using the application.")
            break

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    menu()
