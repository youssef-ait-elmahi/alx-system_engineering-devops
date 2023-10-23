#!/usr/bin/python3
"""
This script uses the requests module to fetch data from a REST API and exports
an employee's TODO list progress to a CSV file.
"""

import csv
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

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                user.get('username'),
                task.get('completed'),
                task.get('title')
            ])
