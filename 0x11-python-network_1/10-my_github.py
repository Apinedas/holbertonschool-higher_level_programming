#!/usr/bin/python3
'''Uses GITHUB API to retrieve user id'''

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
