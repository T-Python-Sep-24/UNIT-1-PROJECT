from datetime import datetime  

class Project:
    # Define project status options as a class-level attribute
    STATUS_OPTIONS = ["Not Started", "In Progress", "Completed", "On Hold"]

    def __init__(self, name, description, start_date, end_date, team_members):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.team_members = team_members
        self.tasks = []  # Add a list to store tasks

    @staticmethod
    def is_valid_date(date_str):
        from datetime import datetime
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False


    def update_project(self, new_name, new_description, new_start_date, new_end_date, new_team_members, new_status):
        """Update project details."""
        self.name = new_name
        self.description = new_description
        self.start_date = new_start_date
        self.end_date = new_end_date
        self.team_members = new_team_members
        self.status = new_status  # Update project status
        print(f"Project '{self.name}' has been updated successfully.")

    def display_project_details(self):
        """Display all details about the project."""
        print(f"Project Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Team Members: {', '.join(self.team_members)}")
        print(f"Status: {self.status}")  # Display project status
        print("-" * 40)

    def delete_project(self):
        """Mark the project for deletion."""
        print(f"Project '{self.name}' has been marked for deletion.")