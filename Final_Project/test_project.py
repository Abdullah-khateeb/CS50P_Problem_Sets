# test_project.py

import pytest
from project import create_task, display_tasks, mark_completed, task_list

def test_create_task():
    create_task("Complete Python homework")
    assert len(task_list) == 1
    assert task_list[0]['description'] == "Complete Python homework"
    assert task_list[0]['is_done'] is False

def test_display_tasks():
    create_task("Buy groceries")
    create_task("Attend meeting")
    tasks = display_tasks()
    assert len(tasks) == 3  # including the task from previous test
    assert tasks[1]['description'] == "Buy groceries"
    assert tasks[2]['description'] == "Attend meeting"

def test_mark_task_as_completed():
    create_task("Complete project")
    result = mark_completed("Complete project")
    assert result is True
    assert task_list[3]['is_done'] is True

def test_mark_non_existent_task():
    result = mark_completed("Non-existent task")
    assert result is False
