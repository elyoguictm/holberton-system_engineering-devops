#!/usr/bin/python3
"""0. Gather data from an API"""

import requests
from sys import argv

if __name__ == '__main__':
    us = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(us)).json()
    al = requests.get(url + "todos?userId={}".format(us)).json()
    tasks = []
    name = u.get('name')

    for task in al:
        if task.get("completed") is True:
            tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(len(name), len(tasks), len(al)))

    print("\n".join("\t {}".format(task) for task in tasks))
