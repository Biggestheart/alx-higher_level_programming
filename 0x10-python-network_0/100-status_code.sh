#!/bin/bash
# sends_a_request_to_a_URL, 
curl -s -o /dev/null -w "%{http_code}" "$1"
