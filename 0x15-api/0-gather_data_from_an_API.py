#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user_res = requests.get(url + "users/{}".format(employee_id))
    user = user_res.json()
    params = {"userId": employee_id}
    todo_res = requests.get(url + "todos", params=params)
    todos = todo_res.json()

    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
          len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
