
# Task Manager Application

#### Video Demo:  <[https://youtu.be/pl4BkM39tT4]>

#### Description:

The **Task Manager Application** is a simple yet functional Python project designed to help users manage their tasks. The application provides an interactive command-line interface (CLI) to create, view, and mark tasks as completed. It serves as a basic example of how a task management system can be implemented in Python, offering a hands-on opportunity to learn and understand the concepts of functions, lists, and user input handling.

### Project Features:
1. **Add a New Tasks**: Users can add tasks to a list by providing a task description.
2. **Show all Tasks**: The task list can be viewed along with the status (whether completed or pending).
3. **Complete a task**: Tasks can be marked as completed by the user when they finish a task.
4. **Exit**: The program allows users to exit the task manager.

### Project Breakdown:

The task manager is implemented using Python and includes several key components:

1. **project.py**: This file contains the core functionality of the application. It defines:
   - `create_task(description)`: A function to add a new task to the task list.
   - `display_tasks()`: A function to show all tasks with their completion status.
   - `mark_completed(description)`: A function to mark a specific task as completed.
   - `start_task_manager()`: The main function that drives the user interface and interacts with the user through the terminal.

2. **test_project.py**: This file contains test cases to validate the core functions in the task manager. The tests are written using the `pytest` framework and ensure that the task manager's functions work as expected. The following tests are included:
   - `test_create_task()`: Tests that tasks are added correctly.
   - `test_display_tasks()`: Tests that tasks are displayed with the correct status.
   - `test_mark_task_as_completed()`: Tests that tasks are marked as completed.
   - `test_mark_non_existent_task()`: Tests handling when trying to mark a non-existent task as completed.

3. **requirements.txt**: This file lists all the external dependencies required by the project. For this project, the only dependency is `pytest`, which is used for testing purposes.

### Design Decisions:

- **Data Structure**: I chose to use a simple list of dictionaries to store the tasks. Each task is represented as a dictionary with the task description and a boolean value (`is_done`) to track whether it has been completed. This makes it easy to manage tasks and check their status.

- **CLI Interface**: I opted for a command-line interface for this project as it provides a straightforward way to interact with the user without introducing complexity. This also allows the user to add, view, and mark tasks without the need for a graphical user interface (GUI).

- **Modular Functions**: The functions were designed to be modular to make the code reusable and testable. For example, the task creation, display, and completion logic were all encapsulated in their own functions, which makes it easier to maintain and expand the project in the future.

- **Testing with `pytest`**: To ensure that the core functionality works as expected, I used `pytest` to write test cases for key functions. This helps in automating the testing process and validating that no bugs are introduced when changes are made.

### Future Improvements:

While the current implementation is simple and functional, there are several ways the project can be enhanced:
- **Priority Levels**: It could be useful to allow users to assign priority levels to tasks, helping them manage important tasks more effectively.
- **Graphical User Interface (GUI)**: A GUI could be implemented to make the task manager more user-friendly, especially for non-technical users.

### How to Use:

1. **Install Dependencies**: Run the following command to install `pytest`:
   ```bash
   pip install -r requirements.txt


### Author : Abdullah Khateeb.
