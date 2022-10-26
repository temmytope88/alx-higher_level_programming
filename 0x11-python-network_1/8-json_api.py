#!/usr/bin/python3
""" A module the uses the requests
module for http request """
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (sys.argv[2]):
        q = sys.argv[2]
    else:
        q = ""

    data = {"q": q}
    r = requests.post(url, data)

    try:
        data = r.json()
        if len(data) > 0:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
