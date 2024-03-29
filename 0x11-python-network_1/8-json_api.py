#!/usr/bin/python3
""" A module the uses the requests
module for http request """
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""

    data = {"q": q}
    r = requests.post(url, data=data)

    try:
        info = r.json()
        if len(info) > 0:
            print("[{}] {}".format(info["id"], info["name"]))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
