#!/usr/bin/python3
"""extend your Python script to export data in the JSON format
"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(argv[1])).json()
    name_user = user['name']

    tasks = []
    for task in todos:
        json_format = {}
        json_format["task"] = task.get("title")
        json_format["completed"] = task.get("completed")
        json_format["username"] = name_user
        tasks.append(json_format)
        json_tasks_format = {}
        json_tasks_format[argv[1]] = tasks
    with open("{}.json".format(argv[1]), "w") as json_file:
        json.dump(json_tasks_format, json_file)
