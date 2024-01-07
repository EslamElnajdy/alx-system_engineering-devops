#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json


if __name__ == "__main__":
    id = int(argv[1])
    res1 = get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user_data = res1.json()
    employee = user_data["username"]

    res2 = get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    todo_data = res2.json()

    row = []
    for i in todo_data:
        new_dict = {}
        new_dict['task'] = i['title']
        new_dict['username'] = employee
        new_dict['completed'] = i['completed']
        row.append(new_dict)

    final_dict = {}
    final_dict[id] = row
    json_obj = json.dumps(final_dict, indent=4)
    id = f"{id}"
    with open(id + ".json", "w") as f:
        f.write(json_obj)
