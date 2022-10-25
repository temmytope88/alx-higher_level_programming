#!/usr/bin/python3
""" a module of http request
using request package """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    header = r.headers.get('X-Request-Id')
    # alternative: r.headers['X-Request-Id']
    print(header)
