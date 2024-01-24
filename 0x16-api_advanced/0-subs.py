#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            subscribers_count = response.json()['data']['subscribers']
            return subscribers_count
        except KeyError:
            print("Error: invalid response format.")
            return 0
    else:
        print(f'Error: {response.status_code}')
        return 0
