#!/usr/bin/python3
"""
This script uses the requests module to fetch data from a REST API and exports
an employee's TODO list progress to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(user_id)).json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
