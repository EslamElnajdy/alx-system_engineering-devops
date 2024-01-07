#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    id = int(argv[1])
    res1 = get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user_data = res1.json()
    employ_n = user_data["name"]

    res2 = get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    todo_data = res2.json()

    total_tasks = len(todo_data)
    done_task = 0
    tasks = []
    for task in todo_data:
        if task["completed"]:
            done_task += 1
            tasks.append(task["title"])

    print("Employee {} is done with tasks({}/{}):".format(employ_n, done_task,
                                                          total_tasks))
    for task in tasks:
        print(f"\t {task}")
