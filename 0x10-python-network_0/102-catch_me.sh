#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: School"
