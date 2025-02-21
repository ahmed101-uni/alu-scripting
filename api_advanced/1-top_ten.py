#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the top ten hot posts from a subreddit.
    If the subreddit is invalid or has no posts, prints None.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent to avoid request rejection

    response = requests.get(
        url,
        params={"limit": 10},  # Limit response to 10 posts
        allow_redirects=False,  # Prevent redirects to search results
        headers=headers,
    )

    # If subreddit is invalid, print None
    if response.status_code != 200:
        print(None)
        return

    try:
        jsonData = response.json()
        data = jsonData.get("data", {}).get("children", [])

        if not data:  # If subreddit exists but has no posts
            print(None)
            return

        for post in data[:10]:  # Print exactly 10 posts
            print(post.get("data", {}).get("title"))

    except ValueError:  # Handle JSON decoding errors (e.g., malformed response)
        print(None)
