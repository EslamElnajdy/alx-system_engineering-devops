#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    id = int(argv[1])
    res1 = get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user_data = res1.json()
    employee = user_data["username"]

    res2 = get(f"https://jsonplaceholder.typicode.com/todos?userId={id}")
    todo_data = res2.json()

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in todo_data:
            row = []
            row.append(i['userId'])
            row.append(employee)
            row.append(i['completed'])
            row.append(i['title'])

            writ.writerow(row)
