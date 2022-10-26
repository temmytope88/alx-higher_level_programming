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
    #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
    #sys.argv[2]
    #header = {"Authorization": "token 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"}
    r = requests.get(url, auth=HTTPBasicAuth(username, token))
    info = r.json()
    print(len(info))
    print(info)
