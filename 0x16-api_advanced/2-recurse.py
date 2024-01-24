#!/usr/bin/python3
""" reddit API """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    global after

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'CustomUserAgent'}
    params = {'after': after}

    response = requests(url, params=params, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title in all_titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return None
