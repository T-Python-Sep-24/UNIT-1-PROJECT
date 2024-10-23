from project import Project  

class Manager:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.projects = []  

def manager_dashboard(self):
        while True:
            print("\nManager Dashboard\n")
            print("Choose an option:")
            print("1. View All Projects")
            print("2. Search Team Tasks")
            print("3. Create Project")
            print("4. Update Project")
            print("5. Delete Project")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.view_all_projects()
            elif choice == "2":
                self.search_team_tasks()
            elif choice == "3":
                self.create_project() 
            elif choice == "4":
                self.update_project()
            elif choice == "5":
                self.delete_project()
            elif choice == "6":
                print("Exiting Manager Dashboard.")
                break
            else:
                print("Invalid option. Please enter a number between 1 and 6.")


def create_project(self):
        try:
            print("\n--- Create New Project ---")  # Debug statement

            name = input("Enter project name: ")
            description = input("Enter project description: ")
            start_date = input("Enter project start date (YYYY-MM-DD): ")
            end_date = input("Enter project end date (YYYY-MM-DD): ")
            team_members = input("Enter team members (comma-separated): ").split(",")

            # Validate the date format
            if Project.is_valid_date(start_date) and Project.is_valid_date(end_date):
                project = Project(name, description, start_date, end_date, team_members)
                self.projects.append(project)  # Add the project to the list
                print(f"Project '{name}' created successfully!\n")
            else:
                print("Invalid date format. Please use YYYY-MM-DD.")
        except Exception as e:
            print(f"An error occurred while creating the project: {e}")
            
def view_all_projects(self):
        if not self.projects:
            print("No projects available.")
            return

        print("\n--- View All Projects ---")
        for idx, project in enumerate(self.projects, start=1):
            print(f"\nProject {idx}:")
            print(f"  Name: {project.name}")
            print(f"  Description: {project.description}")
            print(f"  Start Date: {project.start_date}")
            print(f"  End Date: {project.end_date}")
            print(f"  Team Members: {', '.join(project.team_members)}")

def update_project(self):
        if not self.projects:
            print("No projects available to update.")
            return

        print("\n--- Update Project ---")
        # Display all projects to the user
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. {project.name} (Start: {project.start_date}, End: {project.end_date})")

        try:
            project_index = int(input("Enter the number of the project you want to update: ")) - 1
            if project_index < 0 or project_index >= len(self.projects):
                print("Invalid project number.")
                return

            project = self.projects[project_index]

            # Update project details
            print("\nEnter new details for the project. Leave blank to keep the current value.")
            new_name = input(f"Current Name: {project.name}\nNew Name: ").strip()
            new_description = input(f"Current Description: {project.description}\nNew Description: ").strip()
            new_start_date = input(f"Current Start Date: {project.start_date}\nNew Start Date (YYYY-MM-DD): ").strip()
            new_end_date = input(f"Current End Date: {project.end_date}\nNew End Date (YYYY-MM-DD): ").strip()
            new_team_members = input(f"Current Team Members: {', '.join(project.team_members)}\nNew Team Members (comma-separated): ").strip()

            # Update only if new values are provided
            if new_name:
                project.name = new_name
            if new_description:
                project.description = new_description
            if new_start_date and Project.is_valid_date(new_start_date):
                project.start_date = new_start_date
            if new_end_date and Project.is_valid_date(new_end_date):
                project.end_date = new_end_date
            if new_team_members:
                project.team_members = [member.strip() for member in new_team_members.split(",")]

            print(f"Project '{project.name}' updated successfully!\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        except Exception as e:
            print(f"An error occurred while updating the project: {e}")

def view_team_tasks(self):
    if not self.projects:
        print("No projects available to view team tasks.")
        return

    print("\n--- View Team Tasks ---")
    for idx, project in enumerate(self.projects, start=1):
        print(f"\nProject {idx}: {project.name}")
        if hasattr(project, 'tasks') and project.tasks:
            for task_idx, task in enumerate(project.tasks, start=1):
                print(f"  Task {task_idx}: {task}")
        else:
            print("  No tasks available for this project.")


    def search_team_tasks(self):
        print("Searching team tasks... (Not implemented)")

    def delete_project(self):
        if not self.projects:
            print("No projects available to delete.")
            return

        print("\n--- Delete Project ---")
        # Display all projects to the user
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. {project.name} (Start: {project.start_date}, End: {project.end_date})")

        try:
            project_index = int(input("Enter the number of the project you want to delete: ")) - 1
            if project_index < 0 or project_index >= len(self.projects):
                print("Invalid project number.")
                return

            deleted_project = self.projects.pop(project_index)
            print(f"Project '{deleted_project.name}' deleted successfully!\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

        except Exception as e:
            print(f"An error occurred while deleting the project: {e}")
