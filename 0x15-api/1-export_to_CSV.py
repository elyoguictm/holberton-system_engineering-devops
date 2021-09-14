#!/usr/bin/python3
"""Script that returns info about employee ID"""
import requests
from sys import argv
import csv

if __name__ == '__main__':
    us = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(us)).json()
    al = requests.get(url + "todos?userId={}".format(us)).json()
    tasks = []
    filename = us + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        taskw = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    for task in al:
        taskw.writerow([int(us),
                        u.get('username'),
                        task.get('completed'),
                        task.get('title')])
