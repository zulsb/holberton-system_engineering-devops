#!/usr/bin/python3
"""Module that export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         params={"id": int(argv[1])})
    username = users.json()[0].get("username")

    to_dos = requests.get("https://jsonplaceholder.typicode.com/todos",
                          params={"userId": int(argv[1])})
    list_dict = to_dos.json()
    for d in list_dict:
        d["task"] = d.pop("title")
        d["username"] = username
        d.pop("userId")
        d.pop("id")

    dict_json = {argv[1]: list_dict}
    with open("{}.json".format(argv[1]), "w") as f:
        str_json = json.dumps(dict_json)
        f.write(str_json)
