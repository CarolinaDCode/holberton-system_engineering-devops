#!/usr/bin/python3
'''
Returns information about his/her list progress.
'''
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(argv[1])).json()

    completed = []
    for task in todos:
        if task.get("completed"):
            completed.append(task.get("title"))
    print("Employee {} is done  with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))

    for task_done in completed:
        print("\t {}".format(task_done))
