#!/usr/bin/python3
""" a module of http request
using request package """
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    b = type(r.text)
    c = r.text
    print('Body response:')
    print('\t- type: {}'.format(b))
    print('\t- content: {}'.format(c))
