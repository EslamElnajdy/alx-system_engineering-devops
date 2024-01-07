#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res1 = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    user_data = res1.json()
    employ_name = user_data["name"]

    res2 = get(f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")
    todo_data = res2.json()

    total_tasks = len(todo_data)
    done_task = 0
    for task in todo_data:
        if task["completed"]:
            done_task += 1

    print(f"Employee {employ_name} is done with tasks\
          ({done_task}/{total_tasks})")
    for task in todo_data:
        print(f"\t{task['title']}")
