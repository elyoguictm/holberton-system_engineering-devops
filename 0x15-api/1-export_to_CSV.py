#!/usr/bin/python3
"""Script that returns info about employee ID"""
import requests
from sys import argv
import csv


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1])).json()
    alll = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()
    tasks = []
    filename = argv[1] + ".csv"

    with open(filename, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in alll:
            taskwriter.writerow([int(argv[1]),
                                 user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
