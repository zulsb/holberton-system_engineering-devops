#!/usr/bin/python3
"""Module that export to JSON"""
from json import dump
import requests
from requests import get
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    to_dos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    json_file = {}
    for u in users:
        _id = u.get("id")
        json_file[_id] = []
        for task in to_dos:
            if task.get("userId") == _id:
                json_file[_id].append({"username": u.get("username"),
                                       "task": task.get("title"),
                                       "completed": task.get("completed")})
    del users, to_dos
    with open("todo_all_employees.json", "w") as f:
        dump(json_file, f)
