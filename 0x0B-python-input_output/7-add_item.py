#!/usr/bin/python3
"""Module for a script that
    adds all the arguments to a python list and
    save them to a file
"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]

if os.path.exists(filename):
    load_from_json_file(filename)

save_to_json_file(args, filename)
