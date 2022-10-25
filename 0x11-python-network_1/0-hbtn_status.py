#!/usr/bin/python3
""" A module for displaying
the body of HTTP request"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.\
         urlopen("https://alx-intranet.hbtn.io/status") as response:

        c = response.read()
        a = type(c)
        b = c.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(a))
        print("\t- content: {}".format(c))
        print("\t- utf8 content: {}".format(b))
