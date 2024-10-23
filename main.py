from Team import ProductOwner, DevTeam, QualityAssurance, UiUx, Task, update_task_status
from rich.console import Console
from rich.table import Table

if __name__ == "__main__":
    team_members = {
        "Product Owner": ProductOwner(),
        "Developer": DevTeam(),
        "QA": QualityAssurance(),
        "UI/UX": UiUx()
    }
current_user=None
while current_user is None:
    role_input = input("Enter your role (Product Owner, Developer, QA, UI/UX): ")
    current_user = team_members.get(role_input)

    if current_user:
        print(f"Logged in as {current_user.role} (ID: {current_user.emID})")


    while current_user:
        cont = input("Choose an option - " +
                     ("Add task (a), " if current_user.role == "Product Owner" else "") +
                     "View tasks (v), Update task (u), Exit (e): ")

        if cont == 'a' and current_user.role == "Product Owner":
            task_des = input("Enter your task: ")
            task_type = input("Task type (hold, ready, in progress, done): ").strip().lower()
            assigned_role = input("Assigned team role: ")
            assigned_to = team_members.get(assigned_role)

            if assigned_to:
                new_task = Task(task_des, task_type, assigned_to)
                new_task.save_task()
                assigned_to.assign_task_to_role(new_task)
                print(f"Task '{task_des}' assigned to {assigned_to.role}.")
            else:
                print("Team role not found.")

        elif cont == 'v':
            tasks = Task.load_tasks()
            if tasks:
                table = Table(title="Task List")
                table.add_column("Task ID", justify="center", style="cyan")
                table.add_column("Description", justify="center", style="magenta")
                table.add_column("Type", justify="center", style="yellow")
                table.add_column("Assigned To", justify="center", style="white")
                for task in tasks:
                    if isinstance(task, Task) and (
                            current_user.role == "Product Owner" or task.assigned_to.role == current_user.role):
                        table.add_row(str(task.task_id), task.task_des, task.task_type,
                                      f"{task.assigned_to.role} (ID: {task.assigned_to.emID})")
                Console().print(table)
            else:
                Console().print("[bold red]No tasks found.[/bold red]")

        elif cont == 'u':
            update_task_status()

        elif cont == 'e':
            print("Goodbye!")
            break

        else:
            print("Please try again.")
