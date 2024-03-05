#!/usr/bin/python3

""" task 0 """

import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
