#!/bin/bash
# Sends_a JSON_POST_request to_a_given URL with_a given_JSON_file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
