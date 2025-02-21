#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the top ten hot posts from a subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params={"limit": 10},  # Ensure only 10 posts are fetched
        allow_redirects=False,
        headers=headers,
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        jsonData = response.json()
        data = jsonData.get("data", {}).get("children", [])

        if not data:  # Check if the list is empty
            print(None)
            return

        for post in data[:10]:  # Print exactly 10 posts
            print(post.get("data", {}).get("title"))

    except ValueError:  # Handle JSON decoding errors
        print(None)
