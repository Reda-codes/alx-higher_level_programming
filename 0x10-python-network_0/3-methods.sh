#!/bin/bash
# Script that takes a URL and displays the size of the body
curl -sI "$1" | grep Allow | cut -d " " -f2
