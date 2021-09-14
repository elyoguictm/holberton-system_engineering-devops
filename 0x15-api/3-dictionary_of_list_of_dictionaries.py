#!/usr/bin/python3
"""Script that returns info about employee ID"""

import requests
import json

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url +"users").json()
    alll = requests.get(url + "todos").json()
    tasksd = {}
    taskend = {}
    filename = 'todo_all_employees.json'

    for data in user:
        nickid = data.get("id")
        tasksd[nickid] = []
        taskend[nickid] = data.get('username')
    for data2 in alll:
        nickid = data2.get("userId")
        datas = {}
        datas["task"] = data2.get('title')
        datas["completed"] = data2.get('completed')
        datas["username"] = taskend.get(nickid)
        tasksd.get(nickid).append(datas)
    with open(filename, 'w') as f:
        json.dump(tasksd, f)
