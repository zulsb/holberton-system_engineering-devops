#!/usr/bin/python3
"""Module that export to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         params={"id": int(argv[1])})
    username = users.json()[0].get("username")

    to_dos = requests.get("https://jsonplaceholder.typicode.com/todos",
                          params={"userId": int(argv[1])})
    list_dict = to_dos.json()
    total_all_task = len(list_dict)

    for d in list_dict:
        d["username"] = username
        d.pop("id")

    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for d in list_dict:
            writer.writerow(d)
