#!/usr/bin/python3
if __name__ == "__main__":
        from calculator_1 import add, sub, mul, div

        a = 10
        b = 5

        output_add = add(a, b)
        output_sub = sub(a, b)
        output_mul = mul(a, b)
        output_div = div(a, b)

        print("{} + {} = {}".format(a, b, output_add))
        print("{} - {} = {}".format(a, b, output_sub))
        print("{} * {} = {}".format(a, b, output_mul))
        print("{} / {} = {}".format(a, b, output_div))

