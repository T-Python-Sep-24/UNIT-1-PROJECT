from datetime import datetime
import re
import uuid

def is_valid_date(date_str):
    """Check if the date matches the YYYY-MM-DD format."""
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", date_str))

class Task:
    STATUSES = ["Not Started", "In Progress", "On Hold", "Completed", "Cancelled"]

    def __init__(self, name, description, task_type, date, status):
        self.id = str(uuid.uuid4())  # Generate a unique ID for the task
        self.name = name
        self.description = description
        self.task_type = task_type
        self.date = date
        self.status = status
        self.created_at = self.get_current_datetime()  # Store the creation time

    @staticmethod
    def get_current_datetime():
        """Return the current date and time formatted as YYYY-MM-DD HH:MM:SS."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_task(self, new_name, new_description, new_task_type, new_task_date, new_status):
        """Update the task details."""
        self.name = new_name
        self.description = new_description
        self.task_type = new_task_type
        self.date = new_task_date
        self.status = new_status
        print(f"Task '{self.name}' has been updated successfully.")

    def display_task_details(self):
        """Display the details of the task."""
        print(f"Task ID: {self.id}")
        print(f"Task Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Task Type: {self.task_type}")
        print(f"Task Date: {self.date}")
        print(f"Task Status: {self.status}")
        print(f"Created At: {self.created_at}")
        print("-" * 40)

class Employee:
    def __init__(self, username):
        self.username = username
        self.tasks = []  # List to store tasks for this employee

    def employee_dashboard(self):
        while True:
            print("\nEmployee Dashboard\n")
            print("1. Create Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Search Task by Name")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.search_task_by_name()
            elif choice == "6":
                print("Exiting Employee Dashboard.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def create_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_type = input("Enter task type: ")
        task_date = input("Enter task date (YYYY-MM-DD): ")
        task_status = input("Enter task status (Not Started, In Progress, On Hold, Completed, Cancelled): ")
        
        if not is_valid_date(task_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        if task_status not in Task.STATUSES:
            print("Invalid status. Please choose a valid status.")
            return

        new_task = Task(task_name, task_description, task_type, task_date, task_status)
        self.tasks.append(new_task)
        print(f"Task '{task_name}' created successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx}:")
            task.display_task_details()

    def update_task(self):
        if not self.tasks:
            print("No tasks available to update.")
            return
        self.view_tasks()
        try:
            task_index = int(input("Enter the number of the task you want to update: ")) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return

            task = self.tasks[task_index]
            new_name = input(f"Enter new task name (current: {task.name}): ").strip() or task.name
            new_description = input(f"Enter new task description (current: {task.description}): ").strip() or task.description
            new_task_type = input(f"Enter new task type (current: {task.task_type}): ").strip() or task.task_type
            new_task_date = input(f"Enter new task date (current: {task.date}, format: YYYY-MM-DD): ").strip() or task.date
            new_status = input(f"Enter new task status (current: {task.status}): ").strip() or task.status

            if new_task_date and not is_valid_date(new_task_date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

            if new_status not in Task.STATUSES:
                print("Invalid status. Please choose a valid status.")
                return

            task.update_task(new_name, new_description, new_task_type, new_task_date, new_status)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_task(self):
        if not self.tasks:
            print("No tasks available to delete.")
            return
        self.view_tasks()
        try:
            task_index = int(input("Enter the number of the task you want to delete: ")) - 1
            if task_index < 0 or task_index >= len(self.tasks):
                print("Invalid task number.")
                return
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task.name}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def search_task(self):
        task_name = input("Enter the task name to search: ").strip()
        found_tasks = [task for task in self.tasks if task_name.lower() in task.name.lower()]

        if found_tasks:
            print("\n--- Search Results ---")
            for idx, task in enumerate(found_tasks, start=1):
                print(f"Task {idx}:")
                task.display_task_details()
        else:
            print(f"No tasks found with the name '{task_name}'.")
