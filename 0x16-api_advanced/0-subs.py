#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            subscribers_count = response.json()['data']['subscribers']
            return subscribers_count
        except KeyError:
            print("Error: invalid response format.")
    elif response.status_code == 404:
        return 0
    else:
        print(f'Error: {response.status_code}')
        return 0
