#!/usr/bin/python3
"""Module that returns the number of total subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit and
       return 0 if invalid subreddit given"""

    headers = {"User-Agent": "Luz"}
    r = requests.get("https://www.reddit.com/r/{}/about.json".
                     format(subreddit), headers=headers)
    if not r:
        return 0
    return(r.json().get("data").get("subscribers"))
