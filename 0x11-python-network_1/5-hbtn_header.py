#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status and print X-Request-Id'''


import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
