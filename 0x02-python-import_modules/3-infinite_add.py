#!/usr/bin/python3
import sys


def add_args():
    sum = 0
    args = sys.argv
    for i in range(1, len(args)):
        sum += int(args[i])
    print(sum)


if __name__ == "__main__":
    add_args()
