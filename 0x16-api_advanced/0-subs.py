#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Function that returns the number of
    subscribers of the reddit API
    """
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'MyAPI/0.0.1'},
                       allow_redirects=False).json()
    try:
        return (req.get('data').get('subscribers'))
    except():
        return 0
