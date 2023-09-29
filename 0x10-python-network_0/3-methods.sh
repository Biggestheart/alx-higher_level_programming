#!/bin/bash
# display_all_HTTP methods_the_server_will_accept_uing_curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
