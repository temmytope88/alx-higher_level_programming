#!/usr/bin/python3
""" A module the uses the requests
module for http request """
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".\
        format(owner, repository)

    r = requests.get(url)
    info = r.json()

    try:
        if len(info) >= 10:
            for i in range(0, 10):
                data = info[i]
                sha = data.get('sha')
                name = data.get('commit').get('author').get('name')
                print("{}: {}".format(sha, name))
        else:
            length = len(info)
            for i in range(0, length):
                data = info[i]
                sha = data.get("sha")
                name = data.get('commit').get('author').get('name')
                print("{}: {}".format(sha, name))          
    except KeyError as e:
        print("None")
