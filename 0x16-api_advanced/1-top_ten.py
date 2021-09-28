#!/usr/bin/python3
"""
Write a function that queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API"""
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'topTen/0.0.1 (by /u/Franklayn)'}
    r = requests.get(url, headers=headers, params={'limit': 10}).json()
    red = r.get("data", {}).get("children", None)
    if red is None:
        print(None)
    else:
        for posts in red:
            print(posts.get('data').get('title'))
