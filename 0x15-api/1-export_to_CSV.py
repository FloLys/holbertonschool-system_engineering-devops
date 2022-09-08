#!/usr/bin/python3
""" Gathers data from API and exports it to CSV format """


import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    done_tasks = 0
    total_tasks = 0

    user_tasks = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(user_id)).json()
    user_name = requests.get(
               'https://jsonplaceholder.typicode.com/users/{}'
               .format(user_id)).json()

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            headers = [task.get('userId'),
                       user_name.get('username'),
                       task.get('completed'),
                       task.get('title')]
            writer.writerow(headers)
