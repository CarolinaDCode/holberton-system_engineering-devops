#!/usr/bin/python3
"""
Top Ten
"""
import json
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the top 10 popular posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    req = requests.get(URL, headers={'User-agent': 'url'},
                       allow_redirects=False).json()
    try:
        lists = req.get('data').get('children')
        for i in lists:
            print(i.get('data').get('title'))
    except:
        print(None)
