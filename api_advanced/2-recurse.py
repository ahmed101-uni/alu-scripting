#!/usr/bin/python3
"""
The module recursively retrieves the titles
of hot posts from a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves the titles of hot
    posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "limit": 100}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()
    children = data["data"]["children"]

    if not children:
        return hot_list

    for child in children:
        hot_list.append(child["data"]["title"])

    after = data.get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
