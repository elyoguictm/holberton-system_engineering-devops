#!/usr/bin/python3
"""Script that returns info about employee ID"""
import requests
from sys import argv
import json

if __name__ == '__main__':
    us = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(us)).json()
    alll = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(us)).json()
    tasks = []
    nick = user.get('username')
    taskend = {}
    taskend[argv[1]] = tasks
    filename = argv[1] + ".json"

    for data in alll:
        tasksd = {}
        tasksd["task"] = data.get('title')
        tasksd["completed"] = data.get('completed')
        tasksd["username"] = nick
        tasks.append(tasksd)
    with open(filename, 'w') as f:
        json.dump(taskend, f)
