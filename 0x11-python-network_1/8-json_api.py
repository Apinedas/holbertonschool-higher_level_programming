#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status and print X-Request-Id'''

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) >= 2:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        retrieved = r.json()
        if len(retrieved) > 0:
            print("[{}] {}".format(retrieved['id'], retrieved['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
