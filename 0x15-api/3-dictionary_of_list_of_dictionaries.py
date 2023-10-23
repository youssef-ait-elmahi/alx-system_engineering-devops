#!/usr/bin/python3
"""
This script uses the requests module to fetch data from a REST API and exports
all employees' TODO list progress to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_tasks = {}
    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')
        tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                tasks.append({
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })
        user_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_tasks, jsonfile)
