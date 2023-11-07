#!/usr/bin/python3
""" Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])
    after = data['after']
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
