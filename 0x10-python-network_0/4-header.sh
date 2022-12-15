#!/bin/bash
# Script that takes a URL, and sends a GET request to the URL
curl -sL -H "X-School-User-Id: 98"  -X GET "$1"
