#!/usr/bin/python3
"""
Accepts_a_URL, sends_a_request to_the URL and_shows the value of the
X-Request-Id_variable found_in the_header of_the_response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
