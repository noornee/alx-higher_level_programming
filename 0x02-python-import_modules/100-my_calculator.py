#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator():
    args = sys.argv
    if len(args) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operators = ["+", "-", "*", "/"]
        if args[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            op = args[2]
            if op == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif op == "-":
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif op == "*":
                print("{} * {} = {}".format(a, b, mul(a, b)))
            else:
                print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    calculator()
