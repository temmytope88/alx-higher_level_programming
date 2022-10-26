#!/usr/bin/python3
""" A module the uses the requests
module for http request """
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get(url, auth=(HTTPBasicAuth(username, token)))
    info = r.json()

    try:
        print(info["id"])
    except KeyError as e:
        print("None")
