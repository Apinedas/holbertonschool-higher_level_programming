#!/usr/bin/python3
'''script that fetches X-Request-Id from argv[1]'''


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        headers = response.headers.items()
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])
