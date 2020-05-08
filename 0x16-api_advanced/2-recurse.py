#!/usr/bin/python3
"""Module that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return all hot articles for a given subreddit and
       return None if invalid subreddit given"""

    headers = {"User-agent": "Luz"}
    r = requests.get("http://www.reddit.com/r/{}/hot.json?after={}".
                     format(subreddit, after), headers=headers)

    if r:
        r = r.json().get("data")
        after = r.get("after")
        r = r.get("children")
        for i in r:
            hot_list.append(i["data"].get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    else:
        return(None)
