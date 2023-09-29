#!/bin/bash
# send_a_request to_an URL with curl, and_displays the_size of_the body_of the_response
curl -s "$1" | wc -c
