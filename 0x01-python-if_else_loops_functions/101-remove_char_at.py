#!/usr/bin/python3

def remove_char_at(str, n):
    """Remove char."""
    arr = []
    if n > len(str) or n < 0:
        return str
    for i in range(len(str)):
        if (str[i] != str[n]):
            arr.append(str[i])
    return ''.join(arr)

