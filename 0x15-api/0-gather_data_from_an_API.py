#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    id_user = int(argv[1])

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    get_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    get_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    
    print('Employee ', end='')

    for user in get_user:
        if id_user == user.get('id'):
            EMPLOYEE_NAME = user.get('name')

    for todo in get_todos:
        total_task = todo.get('userId')
        if total_task == id_user:
            TOTAL_NUMBER_OF_TASKS += 1

            conf_task = todo.get('completed')
            if conf_task is True:
               NUMBER_OF_DONE_TASKS += 1
               TASK_TITLE.append(todo.get('title'))

    print('{} is done with tasks({}/{})'.format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    
    for title in TASK_TITLE:
        print('\t {}'.format(title))
