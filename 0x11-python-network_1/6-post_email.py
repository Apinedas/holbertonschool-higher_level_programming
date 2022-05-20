#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status and print X-Request-Id'''

if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
