#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    id_user = int(argv[1])

    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_title = []

    get_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    get_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    print('Employee ', end='')

    for user in get_user:
        if id_user == user.get('id'):
            employee_name = user.get('name')

    for todo in get_todos:
        total_task = todo.get('userId')
        if total_task == id_user:
            total_number_of_tasks += 1

            conf_task = todo.get('completed')
            if conf_task is True:
                number_of_done_tasks += 1
                task_title.append(todo.get('title'))

    print('{} is done with tasks({}/{})'.format(
        employee_name, number_of_done_tasks, total_number_of_tasks))

    for title in task_title:
        print('\t {}'.format(title))
