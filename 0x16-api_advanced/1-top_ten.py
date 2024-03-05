#!/usr/bin/python3
""" prints the titles of the first 10 hot posts
    listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """get first 10 hot post for a subreddit"""
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        params = {'limit': 10}
        req = requests.get(url, params=params, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)