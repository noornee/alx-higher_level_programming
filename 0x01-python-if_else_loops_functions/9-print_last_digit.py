#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1]
    print(f"{int(last_digit)}", end="")
    return int(last_digit)
