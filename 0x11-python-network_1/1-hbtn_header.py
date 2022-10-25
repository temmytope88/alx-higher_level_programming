#!/usr/bin/python3
""" A module that uses urlib package
for http request """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.\
         urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])
