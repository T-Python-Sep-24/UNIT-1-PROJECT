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
            print("5. Exit")
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting Employee Dashboard.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def create_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        self.tasks.append({'name': task_name, 'description': task_description})
        print(f"Task '{task_name}' created successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task['name']} - {task['description']}")

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
            new_name = input("Enter new task name: ")
            new_description = input("Enter new task description: ")
            self.tasks[task_index]['name'] = new_name
            self.tasks[task_index]['description'] = new_description
            print("Task updated successfully.")
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
            print(f"Task '{deleted_task['name']}' deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
