#!/bin/bash
# Bash script that sends a request to a URL and displays only the status code
curl -sI "$1" | grep HTTP/1.1 | cut -d " " -f2
