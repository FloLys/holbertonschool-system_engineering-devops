#!/usr/bin/python3
""" Reddit API """


def top_ten(subreddit):
    """ Returns top 10 hot post titles of a subreddit """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        posts = response.json().get('data').get('children')
        for elem in posts:
            print(elem.get('data').get('title'))
