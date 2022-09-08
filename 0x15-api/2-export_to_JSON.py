#!/usr/bin/python3
""" Gathers data from API and exports it to JSON format """


import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    done_tasks = 0
    total_tasks = 0
    tasks_owned = []

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_info = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()

    with open('{}.json'.format(user_id), 'w') as json_file:
        for task in user_tasks:
            headers = {'task': task.get('title'),
                       'completed': task.get('completed'),
                       'username': user_info.get('username')}
            tasks_owned.append(headers)

        user_data_dict = {str(user_id): tasks_owned}
        json.dump(user_data_dict, json_file)
