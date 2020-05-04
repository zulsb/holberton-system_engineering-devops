#!/usr/bin/python3
"""Module that gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1]))
    name = users.json().get("name")

    to_dos = requests.get("https://jsonplaceholder.typicode.com/todos",
                          params={"userId": argv[1]})
    list_dict = to_dos.json()
    total_all_task = len(list_dict)

    done_task = []
    for d in list_dict:
        if d.get("completed"):
            done_task.append(d)

    numbers_done_task = len(done_task)

    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          numbers_done_task,
                                                          total_all_task))
    for task in done_task:
        print("\t {}".format(task.get("title")))
