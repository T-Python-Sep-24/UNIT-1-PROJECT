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
            with open('tasks.pkl', 'wb') as file:
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

        console= Console()
        with open('tasks.pkl', 'rb') as file:
            tasks = pickle.load(file)
            table = Table(title="Tasks")

            table.add_column("Hold", justify="center", style="cyan", no_wrap=True)
            table.add_column("Ready", justify="center", style="magenta")
            table.add_column("In progress", justify="center", style="magenta")
            table.add_column("done", justify="center", style="magenta")
            console.print(table, justify="center")
            task_hold=[]
            task_ready=[]
            task_progress=[]
            task_done=[]
            for task  in tasks:
                task_des=task["task_des"]
                task_type=task["task_type"]

                if task_type=="hold":
                    task_hold.append(task_des)


                elif task_type=="ready":
                    task_ready.append(task_des)

                elif task_type=="progress":
                    task_progress.append(task_des)

                elif task_type=="done":
                    task_done.append(task_des)
                else:
                    console.print()
            table_max=max(len(task_hold),len(task_ready),len(task_progress),len(task_done))
            print(table_max)
            for i in range(table_max):
                table.add_row(task_hold[i],task_progress[i],task_ready[i],task_done[i])
            console.print(table,justify="center")
    except Exception as e:
        print(e)



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
