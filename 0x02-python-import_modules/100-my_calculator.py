#!/usr/bin/python3
from typing import Match


if __name__ == "__main__":

    import sys
    import calculator_1 as calc

    argc = len(sys.argv)

    if (argc != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
