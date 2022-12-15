#!/bin/bash
# Script that takes a URL and displays all HTTP methods the server will accept.
curl -sIL -X OPTIONS "$1" | grep Allow: | cut -d ":" -f2 | sed 's/ //'
