#!/usr/bin/python3
"""
Accepts_a URL and_an_email address,_sends_a_POST request_to_the_passed URL
with the_email_as a_parameter, and_finally shows_the body_of the_response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
