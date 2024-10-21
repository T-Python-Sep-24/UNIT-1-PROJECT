import os
import pickle
import subprocess
from rich.console import Console
from rich.table import Table
def fil_ter():
    with open('tasks.pkl', 'rb') as file:
        tasks = pickle.load(file)

class Team:
    emb_id=101
    def __init__(self,task:str,role:str):
        self.task=task
        self.role=role
        self.emID=Team.emb_id

    def card(self):
        pass



class Task:
    def __init__(self,task: str, role: str):
        self.team=Team(task,role)

    @staticmethod
    def task_adding():
        try:
            with open('tasks.pkl', 'rb') as file:
                tasks = pickle.load(file)
        except FileNotFoundError:
            tasks = []
        task_des = str(input("enter your task:"))
        task_type = str(input("type of this task?"))
        new_task = {
            "task_des": task_des,
            "task_type": task_type
        }
        tasks.append(new_task)


def task_return():
    try:
        with open('tasks.pkl', 'rb') as file:
            tasks = pickle.load(file)
            table = Table(title="Tasks")

            table.add_column("Task Description", justify="center", style="cyan", no_wrap=True)
            table.add_column("Task Type", justify="center", style="magenta")
            table.add_column("Ready", justify="center", style="magenta")
            table.add_column("Hold", justify="center", style="magenta")
            table.add_column("In progress", justify="center", style="magenta")
            table.add_column("done", justify="center", style="magenta")


            for task in tasks:
                table.add_row(task["task_des"], task["task_type"])
            console = Console()
            console.print(table, justify="center")
    except Exception as e:
        console.print(e)


class ProductOwner(Team):
    def __init__(self, task: str, role: str):
        super().__init__(task, role)

class DevTeam:
    pass

class QualityAssurance:
    pass
class UiUx:
    pass

if __name__ == "__main__":
    task_manager = Task('default_task', 'default_role')

    while True:
        cont = input("Choose an option - Add task (a), View tasks (v), Exit (e): ")
        if cont.lower() == 'a':
            task_manager.task_adding()
        elif cont.lower() == 'v':
            task_return()
        elif cont.lower() == 'e':
            break
