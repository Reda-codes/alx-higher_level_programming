#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


fileName = "add_item.json"

try:
    obj = load_from_json_file(fileName)
except Exception as e:
    obj = []

for arg in sys.argv[1:]:
    obj.append(arg)

save_to_json_file(obj, fileName)
