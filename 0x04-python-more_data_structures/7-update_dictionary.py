#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if key == k:
            a_dictionary.update({key: value})
    a_dictionary[key] = value
    return a_dictionary
