#!/usr/bin/python3
import requests
import sys
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""


def get_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data")
        sys.exit(1)
    return response.json()


def main(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    base_url = "https://jsonplaceholder.typicode.com/users"
    todos_endpoint = "/{}/todos"
    todos_url = f"{base_url}{todos_endpoint.format(employee_id)}"

    user_data = get_data(user_url)
    todos_data = get_data(todos_url)

    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task.get('completed')])

    print(f"Employee {user_data.get('name')} is done with tasks\
        ({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee ID>'.format(sys.argv[0]))
        sys.exit(1)

    main(sys.argv[1])
