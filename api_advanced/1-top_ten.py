#!/usr/bin/python3
"""
The module prints the titles of the top
10 hot posts from a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetch and print the top 10 hot posts from a subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(
        url,
        params={"limit": 10},  # Limit results to 10 posts
        headers=headers,
        allow_redirects=False  # Prevent following search result redirects
    )

    # If the subreddit is invalid or API fails, return None
    if response.status_code != 200:
        print(None)
        return

    try:
        jsonData = response.json()
        posts = jsonData.get("data", {}).get("children", [])
        
        # If no posts are found, return None
        if not posts:
            print(None)
            return

        # Print top 10 post titles
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except ValueError:  # Handle JSON parsing errors
        print(None)
