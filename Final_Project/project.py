# Project title: "Task Manager";
# Name: Abdullah;
# Github: https://github.com/Abdullah-khateeb;


# A list to store tasks with their completion status
task_list = []

def create_task(description):
    task = {'description': description, 'is_done': False}
    task_list.append(task)

def display_tasks():
    return task_list

def mark_completed(description):
    for task in task_list:
        if task['description'] == description:
            task['is_done'] = True
            return True
    return False

def start_task_manager():
    while True:
        print("Welcome to the Task Manager")
        print("1. Add a New Task")
        print("2. Show All Tasks")
        print("3. Complete a Task")
        print("4. Exit")

        user_choice = input("Select an option (1-4): ")

        if user_choice == '1':
            task_desc = input("Enter the task description: ")
            create_task(task_desc)
        elif user_choice == '2':
            tasks = display_tasks()
            print("Task List:")
            for task in tasks:
                status = "Completed" if task['is_done'] else "Pending"
                print(f"{task['description']} - Status: {status}")
        elif user_choice == '3':
            task_desc = input("Enter the task description to mark as completed: ")
            if not mark_completed(task_desc):
                print("Task not found. Please check the description.")
            else:
                print(f"Task '{task_desc}' has been marked as completed.")
        elif user_choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

# Call the main function to start the task manager
if __name__ == "__main__":
    start_task_manager()
