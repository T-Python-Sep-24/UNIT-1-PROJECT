Trio Tool


Overview: Trio Tool is an interactive Command-Line Interface (CLI) project management tool designed to facilitate task and project management within a team environment. Users can register as either a Manager or a Team Member, each with their own set of functionalities. The application enables efficient task management through features like task creation, updating, and searching. Managers have additional capabilities for overseeing team projects, making Trio Tool an all-encompassing solution for collaborative project tracking and management.


Features

User Roles:

1- Manager:

- Access to a comprehensive Manager Dashboard.

- View all team tasks and filter by username or task details.

- Search for specific team tasks.

- Perform CRUD operations on projects, including adding, updating, deleting, and searching projects.


2- Team Member:

- Create and manage individual tasks.

- Perform CRUD operations on tasks.

- Search tasks by task name or other details.


Core Functionalities:

- Account Creation: Users can register by providing information such as username, email, role, department, and password.

- Task Management: CRUD operations (Create, Read, Update, Delete) for tasks with detailed task information, including name, description, type, status, and date.

- Project Management: Managers can create and manage projects for the team.

- Search: Search functionalities to quickly locate tasks and projects.


User Stories

1- As a Manager, I want to view all the tasks of my team members, so I can monitor their progress and provide support when needed.

2- As a Manager, I want to be able to search for specific tasks by username or task details, so I can quickly find relevant information.

3- As a Manager, I want to create a project, so I can organize and manage team activities effectively.

4- As a Team Member, I want to create, update, and delete tasks, so I can manage my daily responsibilities effectively.

4- As a Team Member, I want to search for my tasks by name or other details, so I can quickly access and organize my work.

5- As a User, I want to create an account with my information, so I can access the tool and use it based on my role.


Usage: 

1- Run the Application:
. Start the program by running: python main.py

2- User Registration:
. Follow the prompts to create an account. You will need to provide: Username , Email , Role (Choose either Manager or Team Member) , Department , Password

3- Manager Commands: 
. View Team Tasks: view_team_tasks
Displays all tasks assigned to team members, filtered by username or task details.

. Search Team Tasks: search_team_tasks username_or_task_name
Search for specific tasks by username or task name.


. Create a Project: create_project project_name project_description project_start_date project_end_date team_members_assigned
Adds a new project to manage team activities.

. Update Project: update_project project_id new_project_name new_project_description new_project_start_date new_project_end_date new_team_members_assigned
Modify details of an existing project.

. Delete Project: delete_project project_id
Remove a project.

. Exit the Manager Dashboard: exit


4- Team Member Commands:
. Create a Task: create_task task_name task_description task_type task_date
Adds a new task with details including name, description, type, and due date.

. View Your Tasks: view_tasks
Lists all tasks you have created.

. Update a Task: update_task task_id new_task_name new_task_description new_task_type new_task_date
Modify an existing task.

. Search Tasks: search_task task_name
Find tasks by task name.

. Delete a Task: delete_task task_id
Remove a task.

. Exit the Task Management Menu: exit




