#!/usr/bin/python3
"""
Accepts  a URL, sends_a_request to_the URL &_displays the_body of_the_response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
