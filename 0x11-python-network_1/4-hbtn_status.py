#!/usr/bin/python3
"""This_python_module holds_a script_that_fetches
https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == "__main__":
    result = get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
