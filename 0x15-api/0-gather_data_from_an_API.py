#!/usr/bin/python3
"""
Write a Python script that, using this REST API
for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':

    u = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv[1])).json()
    al = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                      .format(argv[1])).json()
    tasks = []
    name = u.get('name')
    for task in al:
        if task.get("completed") is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(len(name), len(tasks), len(al)))
    print("\n".join("\t {}".format(task) for task in tasks))
