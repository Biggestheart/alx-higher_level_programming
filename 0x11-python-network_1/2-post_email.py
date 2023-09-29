#!/usr/bin/python3
"""Accepts_a_URL and_an_email, sends_a_POST request_to_the passed_URL with_the
email_as a_parameter, and displays_the body_of_the_response
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
