#!/usr/bin/python3
"""
Accepts_a URL,_sends_a_request to_the URL_and_shows the_value of_the
variable X-Request-Id_in the_response_header
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
