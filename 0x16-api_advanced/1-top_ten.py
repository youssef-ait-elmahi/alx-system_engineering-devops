#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
