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
    def __init__(self, name):
        self.name = name
        self.tasks = []

def create_task(self, task_name, task_description, task_type, task_date):
    """Create a new task."""
    if not is_valid_date(task_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    print("Select a status for the task:")
    for idx, status in enumerate(Task.STATUSES):
        print(f"{idx + 1}: {status}")

    status_choice = int(input("Enter the number corresponding to the status: ")) - 1
    if status_choice < 0 or status_choice >= len(Task.STATUSES):
        print("Invalid choice. Task not created.")
        return

    task_status = Task.STATUSES[status_choice]
    task = Task(task_name, task_description, task_type, task_date, task_status)
    self.tasks.append(task)
    print(f"Task '{task_name}' created successfully.")


    def view_tasks(self, search_term=None):
        """View all tasks or search for specific tasks."""
        found_tasks = [task for task in self.tasks if search_term.lower() in task.name.lower()] if search_term else self.tasks

        if not found_tasks:
            print("No tasks found.")
        else:
            print(f"Tasks for {self.name}:")
            for task in found_tasks:
                task.display_task_details()

    def update_task(self, task_id, new_task_name, new_task_description, new_task_type, new_task_date, new_status):
        """Update an existing task."""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.update_task(new_task_name, new_task_description, new_task_type, new_task_date, new_status)
        else:
            print("Invalid task ID. Please provide a valid ID.")

    def search_task(self, task_name):
        """Search for a task by name."""
        found = False
        for task in self.tasks:
            if task_name.lower() in task.name.lower():
                task.display_task_details()
                found = True
        if not found:
            print(f"No tasks found for the search term '{task_name}'.")

    def delete_task(self, task_id):
        """Delete a task by ID."""
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            confirmation = input(f"Are you sure you want to delete the task '{task.name}'? (yes/no): ").strip().lower()
            if confirmation == "yes":
                self.tasks.remove(task)
                print(f"Task '{task.name}' has been deleted successfully.")
            else:
                print("Deletion canceled.")
        else:
            print("Invalid task ID. Please provide a valid ID.")

    def task_management_menu(self):
        """Display the task management menu and handle user input."""
        while True:
            print("\nChoose from the Options:")
            print("1. Create Task")
            print("2. View/Search Tasks")
            print("3. Update Task")
            print("4. Search Task")
            print("5. Delete Task")
            print("6. Exit")

            option = input("Choose an option (1-6): ")

            if option == "1":
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                task_type = input("Enter task type: ")
                task_date = input("Enter task date (YYYY-MM-DD): ")
                self.create_task(task_name, task_description, task_type, task_date)
            elif option == "2":
                search_term = input("Enter search term (leave blank to view all tasks): ")
                self.view_tasks(search_term)
            elif option == "3":
                task_id = input("Enter task ID to update: ")
                new_task_name = input("Enter new task name: ")
                new_task_description = input("Enter new task description: ")
                new_task_type = input("Enter new task type: ")
                new_task_date = input("Enter new task date (YYYY-MM-DD): ")
                print("Select a new status for the task:")
                for idx, status in enumerate(Task.STATUSES):
                    print(f"{idx + 1}: {status}")
                new_status_choice = int(input("Enter the number corresponding to the new status: ")) - 1
                new_status = Task.STATUSES[new_status_choice] if 0 <= new_status_choice < len(Task.STATUSES) else "Not Started"
                self.update_task(task_id, new_task_name, new_task_description, new_task_type, new_task_date, new_status)
            elif option == "4":
                task_name = input("Enter task name to search: ")
                self.search_task(task_name)
            elif option == "5":
                task_id = input("Enter task ID to delete: ")
                self.delete_task(task_id)
            elif option == "6":
                print("Exiting Task Management Menu.")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.")
