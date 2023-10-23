#!/usr/bin/python3
"""Write a Python script that, using this REST API,"""
import requests
import sys


def get_todo_list_progress(employee_id):
    # Fetch employee data
    employee_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch todo data
    todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = len([task for task in todo_data if task['completed']])
    done_task_titles = [task['title'] for task in todo_data if task
                        ['completed']]

    # Print progress
    print(
            f'Employee {employee_name} is done with tasks'
            f'({done_tasks}/{total_tasks}):'
            )
    for title in done_task_titles:
        print('\t ' + title)


if __name__ == "__main__":
    get_todo_list_progress(int(sys.argv[1]))
