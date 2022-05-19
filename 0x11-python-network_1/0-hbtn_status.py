#!/usr/bin/python3
'''script that fetches https://intranet.hbtn.io/status'''

from encodings import utf_8, utf_8_sig
import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
    print("\t- utf8 content: {}".format(page.decode("utf8")))
