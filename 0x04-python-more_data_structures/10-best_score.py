#!/usr/bin/python3
def best_score(a_dictionary):
    max_num = 0
    if a_dictionary == None:
        return None
    for _, v in a_dictionary.items():
        if v > max_num:
            max_num = v
    return ''.join([k for k, v in a_dictionary.items() if v == max_num])
