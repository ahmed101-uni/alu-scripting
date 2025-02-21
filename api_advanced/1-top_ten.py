#!/usr/bin/python3
"""
The module prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    The function fetches and prints the titles
    of the top 10 hot posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params={"limit": 10},  
        allow_redirects=False,
        headers=headers,
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        jsonData = response.json()
        posts = jsonData.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:  
            print(post.get("data", {}).get("title"))
    except ValueError:  
        print(None)
