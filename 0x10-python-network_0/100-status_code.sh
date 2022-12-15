#!/bin/bash
# Bash script that sends a request to a URL and displays only the status code
curl -sLw "%{http_code}" -o /dev/null "$1"
