#!/usr/bin/python3
""" Reddit API """


def number_of_subscribers(subreddit):
    """ Returns number of suscribers of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code != 200:
        return 0
    return resp.json().get('data').get('subscribers') or 0
