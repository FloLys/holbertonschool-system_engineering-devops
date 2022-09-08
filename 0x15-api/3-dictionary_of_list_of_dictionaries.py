#!/usr/bin/python3
""" Gathers data from API and exports it to JSON format """


import json
import requests
from sys import argv

if __name__ == "__main__":
    done_tasks = 0
    total_tasks = 0
    tasks_dict = {}

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/todos'
                ).json()
    user_info = requests.get(
               'https://jsonplaceholder.typicode.com/users'
               ).json()

    with open('todo_all_employees.json', 'w') as json_file:
        for task in user_tasks:
            user_id = task.get('userId')
            for user in user_info:
                if user['id'] == user_id:
                    username = user['username']
                    break

            headers = {'task': task.get('title'),
                       'completed': task.get('completed'),
                       'username': username}

            if not str(user_id) in tasks_dict.keys():
                tasks_dict[str(user_id)] = []
            tasks_dict[str(user_id)].append(headers)

        json.dump(tasks_dict, json_file)
