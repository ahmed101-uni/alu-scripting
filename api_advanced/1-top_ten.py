#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A function that fetches and prints the titles
    of the top ten hot posts from a subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

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
            print(post.get("data", {}).get("title", None))
    
    except ValueError:  
        print(None)
        