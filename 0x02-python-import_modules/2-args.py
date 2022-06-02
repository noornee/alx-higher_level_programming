#!/usr/bin/python3
import sys


def arguments():
    argv = sys.argv
    args_len = len(argv)
    if args_len == 1:
        print(f"0 arguments.")
    else:
        print(f"{args_len - 1} arguments:")
        for i in range(1, args_len):
            print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    arguments()
