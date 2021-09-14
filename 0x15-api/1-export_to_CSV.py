#!/usr/bin/python3
"""Script that returns info about employee ID"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    us = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}"
    u = requests.get(url + "users/{}".format(argv[1])).json()
    al = requests.get(url + "todos?userId={}".format(argv[1])).json()
    tasks = []
    filename = argv[1] + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        taskw = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in al:
            taskw.writerow([int(argv[1]),
                            u.get('username'),
                            task.get('completed'),
                            task.get('title')])
