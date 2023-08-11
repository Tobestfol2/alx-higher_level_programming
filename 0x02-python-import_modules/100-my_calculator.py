#!/usr/bin/python3
if __name__ == "__main__":
    import sys

from calculator_1 import add, sub, mul, div

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

if op not in ('+', '-', '*', '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

    if op== '+':
        result = add(a, b)
        operator = "+"
    elif op == '-':
        result = sub(a, b)
        operator = "-"
    elif op == '*':
        result = mul(a, b)
        operator = "*"
    else:
        result = div(a, b)
        operator = "/"

    print("{} {} {} = {}".format(a, operator, b, result))
