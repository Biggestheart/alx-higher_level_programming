#!/usr/bin/python3
"""recieves your_Github credentials_(username_and_password)
and_uses_the Github_API
to_dsplay your_id"""
from sys import argv
from requests import get, auth


if __name__ == "__main__":
    auth = auth.HTTPBasicAuth(argv[1], argv[2])
    result = get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
