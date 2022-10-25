#!/usr/bin/python3
""" a module of http request
using request package """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        c = r.text
        print(c)

    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code()))
