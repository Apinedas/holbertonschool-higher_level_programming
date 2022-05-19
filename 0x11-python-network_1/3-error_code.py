#!/usr/bin/python3
'''script that POST email to argv[1]'''


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from urllib.parse import urlencode
    from sys import argv


    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))
