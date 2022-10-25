#!/usr/bin/python3
""" A module that uses the
urllib package and handles exceptions """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.\
             urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        code = e.code
        print("Error code: {}".format(code))
