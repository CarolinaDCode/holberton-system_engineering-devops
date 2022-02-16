#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers 
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    function that performs a request that
    retrieves the number of subscriberst
    """
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'url'},
                       allow_redirects=False).json()
    try:
        return (req.get('data').get('subscribers'))
    except:
        return 0
