from project import Project  

class Manager:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.projects = []  

    def manager_dashboard(self):
        while True:
            print("\nManager Dashboard\n")
            print("Choose an option:")
            print("1. View Team Tasks")
            print("2. Search Team Tasks")
            print("3. Create Project")
            print("4. Update Project")
            print("5. Delete Project")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.view_team_tasks()
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

        name = input("Enter project name: ")
        print(f"Received name: {name}")  # Debugging print

        description = input("Enter project description: ")
        start_date = input("Enter project start date (YYYY-MM-DD): ")
        end_date = input("Enter project end date (YYYY-MM-DD): ")
        team_members = input("Enter team members (comma-separated): ").split(",")

        if Project.is_valid_date(start_date) and Project.is_valid_date(end_date):
            project = Project(name, description, start_date, end_date, team_members)
            self.projects.append(project)  # Add the project to the list
            print(f"Project '{name}' created successfully!")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def view_team_tasks(self):
        print("Displaying team tasks... (Not implemented)")

    def search_team_tasks(self):
        print("Searching team tasks... (Not implemented)")

    def update_project(self):
        print("Updating project... (Not implemented)")

    def delete_project(self):
        print("Deleting project... (Not implemented)")
