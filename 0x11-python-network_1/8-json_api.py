#!/usr/bin/python3
"""
Accepts_a_letter and_sends_a POST_request_to http://0.0.0.0:5000/search_user
with_the_letter as_a_parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = r.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
