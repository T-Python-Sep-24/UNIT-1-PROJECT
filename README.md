Trio Tool


Overview: Trio Tool is an interactive Command-Line Interface (CLI) project management tool designed to facilitate task and project management within a team environment. Users can register as either a Manager or a Team Member, each with their own set of functionalities. The application enables efficient task management through features like task creation, updating, and searching. Managers have additional capabilities for overseeing team projects, making Trio Tool an all-encompassing solution for collaborative project tracking and management.


## Features

### User Roles:

1- **Manager:**

- Access to a comprehensive Manager Dashboard.

- Perform CRUD operations on projects, including adding, updating, deleting, and searching projects.


2- **Team Member:**

- Create and manage individual tasks.

- Perform CRUD operations on tasks.



### Core Functionalities:

- **Account Registration**: Users can register by providing information such as username, email, role, department, and password.

- **Account Login**: Users can log in by providing their username and password.

- **Task Management**: CRUD operations (Create, Read, Update, Delete) for tasks with detailed task information, including name, description, type, status, and date.

- **Project Management**: Managers can perform CRUD operations (Create, Read, Update, Delete) for projects with detailed project information, including name, description, start date, end date, and team members.

- **Search**: Search functionalities to quickly locate projects.




## User Stories

3- As a Manager, I want to create, update, and delete a project, so I can organize and manage team activities effectively.

4- As a Team Member, I want to create, update, and delete tasks, so I can manage my daily responsibilities effectively.

5- As a User, I want to create an account with my information, so I can access the tool and use it based on my role.


## Usage: 

1. **Run the Application:**
   - Start the program by running: `python main.py`

2. **User Registration:**
   - Follow the prompts to create an account. You will need to provide:
     - Username
     - Email
     - Role (Choose either Manager or Team Member)
     - Department
     - Password

3. **Manager Commands:**
   - Create a Project: `create_project project_name project_description project_start_date project_end_date team_members_assigned`
   - Update Project: `update_project project_id new_project_name new_project_description new_project_start_date new_project_end_date new_team_members_assigned`
   - Delete Project: `delete_project project_id`
   - Exit the Manager Dashboard: `exit`

4. **Team Member Commands:**
   - Create a Task: `create_task task_name task_description task_type task_date`
   - View Your Tasks: `view_tasks`
   - Update a Task: `update_task task_id new_task_name new_task_description new_task_type new_task_date`
   - Delete a Task: `delete_task task_id`
   - Exit the Task Management Menu: `exit`



## Library Dependencies

**Trio Tool uses the following libraries:**

datetime: Used for handling and formatting dates and times in tasks and projects.

re: Utilized for validating date formats and other input data.

uuid: Generates unique IDs for tasks and projects, ensuring distinct identification for each item.

json: Handles serialization and deserialization of user and project data.

os: Used for interacting with the operating system, including file handling and environment operations.

bcrypt: Provides hashing functionality for securely storing user passwords.




