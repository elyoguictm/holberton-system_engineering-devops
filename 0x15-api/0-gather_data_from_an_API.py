
#!/usr/bin/python3
"""
Write a Python script that, using this REST API
for a given employee ID, returns
information about his/her list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format
                        (argv[1])).json()
    alll = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    tasks = []
    name = user.get('name')
    for task in alll:
        if task.get("completed") is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(len(name), len(tasks), len(alll)))
    print("\n".join("\t {}".format(task) for task in tasks))
