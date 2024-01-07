#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
import json


if __name__ == "__main__":
    res1 = get(f"https://jsonplaceholder.typicode.com/users")
    user_data = res1.json()

    res2 = get(f"https://jsonplaceholder.typicode.com/todos")
    todo_data = res2.json()

    final_dict = {}
    for i in user_data:
        row = []
        for j in todo_data:
            new_dict = {}
            if j['userId'] == i['id']:
                new_dict['task'] = j['title']
                new_dict['username'] = i['username']
                new_dict['completed'] = j['completed']
                row.append(new_dict)
        final_dict[i['id']] = row

    json_obj = json.dumps(final_dict, indent=4)
    with open('todo_all_employees' + ".json", "w") as f:
        f.write(json_obj)
