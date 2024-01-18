#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

from requests import get


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {
        'User-agent': 'Google Chrome Version 81.0.4044.129'
        }
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params).json()

    try:
        my_data = response.get('data').get('children')

        for each_data in my_data:
            print(each_data.get('data').get('title'))

    except Exception as e:
        print("None")
