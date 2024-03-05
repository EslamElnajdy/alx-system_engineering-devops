#!/usr/bin/python3
"""
returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """get all articles for
        a given subreddit
    """
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        params = {'after': after, 'limit': 100}
        headers = {'user-agent': 'my-app/0.0.1'}

        req = requests.get(url, params=params, headers=headers, allow_redirects=False)

        if req.status_code == 200:
            data = req.json().get('data')
            after = data.get('after')
            posts = data.get('children')

            for post in posts:
                hot_list.append(post.get('data').get('title'))

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
