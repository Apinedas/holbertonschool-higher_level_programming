#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''


import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers.get('X-Request-Id'))
