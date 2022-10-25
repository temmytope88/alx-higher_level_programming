#!/usr/bin/python3
""" a module of http request
using request package """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    r.status_code
    if r.status_code == requests.codes.ok:
        c = r.text
        print(c)
    else:
        print("Error code: {}".format(r.status_code()))
