import pickle
class Team:
    emb_id = 101
    tasks_by_role = {}

    @classmethod
    def generate_id(cls):
        id_us = cls.emb_id
        cls.emb_id += 1
        return id_us

    def __init__(self, role):
        self.role = role
        self.emID = Team.generate_id()

    def assign_task_to_role(self, task):
        try:
            Team.tasks_by_role[self.role].append(task)
        except KeyError:
            Team.tasks_by_role[self.role] = []
            Team.tasks_by_role[self.role].append(task)


class Task:
    task_id = 1
    @classmethod
    def generate_id(cls):
        id_us = cls.task_id
        cls.task_id += 1
        return id_us
    def __init__(self, task_des, task_type, assigned_to):
        self.task_id = Task.generate_id()
        self.task_des = task_des
        self.task_type = task_type
        self.assigned_to = assigned_to

    def display_task(self):
        print(f"Task ID: {self.task_id}")
        print(f"Description: {self.task_des}")
        print(f"Type: {self.task_type}")
        print(f"Assigned To: {self.assigned_to.role} "
            f"(ID: {self.assigned_to.emID})")

    def save_task(self):
        try:
            with open('tasks.pkl', 'rb') as file:
                tasks = pickle.load(file)
        except (FileNotFoundError, EOFError):
            tasks = []
        tasks.append(self)
        with open('tasks.pkl', 'wb') as file:
            pickle.dump(tasks, file)

    @staticmethod
    def load_tasks():
        try:
            with open('tasks.pkl', 'rb') as file:
                tasks = pickle.load(file)
                return tasks
        except (FileNotFoundError, EOFError):
            return None

class ProductOwner(Team):
    def __init__(self):
        super().__init__(role="Product Owner")

class DevTeam(Team):
    def __init__(self):
        super().__init__(role="Developer")

class QualityAssurance(Team):
    def __init__(self):
        super().__init__(role="QA")

class UiUx(Team):
    def __init__(self):
        super().__init__(role="UI/UX")

def update_task_status():
    tasks = Task.load_tasks()

    for task in tasks:
        print(f"Task ID: {Task.generate_id()}, Description: {task.task_des}, Status: {task.task_type}")

    selected_task_id = input("Enter the Task ID you want to update: ")
    selected_task = None

    for task in tasks:
        if str(task.task_id) == selected_task_id:
            selected_task = task
            break

    if selected_task:
        new_status = input("Enter new status (hold, ready, in progress, done): ").strip().lower()
        if new_status in ['hold', 'ready', 'in progress', 'done']:
            selected_task.task_type = new_status
            # Save the updated tasks
            with open('tasks.pkl', 'wb') as file:
                pickle.dump(tasks, file)
            print("Status updated successfully.")
        else:
            print("Invalid status.")
    else:
        print("Invalid Task ID.")
