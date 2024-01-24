#!/usr/bin/python3
""" print the titles of the first 10hot posts """
import requests
import json


def top_ten(subreddit):
    """ print the title of 1st 10hot posts """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-agent': 'CustomUserAgent'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        except Exception:
            return('None')
