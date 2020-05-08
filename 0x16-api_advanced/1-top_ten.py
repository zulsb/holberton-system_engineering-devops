#!/usr/bin/python3
"""Module that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return top ten titles for a given subreddit and
       return None if invalid subreddit given"""

    headers = {"User-Agent": "Luz"}
    r = requests.get("https://www.reddit.com/r/{}/hot/.json".
                     format(subreddit), headers=headers)
    if not r:
        print(None)
    else:
        children = r.json().get("data").get("children")
        for c in range(10):
            print(children[c].get("data").get("title"))
