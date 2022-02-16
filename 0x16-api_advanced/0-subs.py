#!/usr/bin/python3
"""
How many subs?
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and
    returns the number of subscribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'url'},
                       allow_redirects=False).json()
    try:
        return (req.get('data').get('subscribers'))
    except:
        return 0
