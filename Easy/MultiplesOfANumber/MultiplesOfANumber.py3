#!/usr/bin/env python

"""
MULTIPLES OF A NUMBER
CHALLENGE DESCRIPTION:


Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or
 equal to x. Do not use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of two integers,
one list per line. E.g.

13,8
17,16
OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

16
32
"""

from sys import argv


with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


def get_variables():
    for case in test_cases:
        x, n = map(int, case.split(','))
        print(get_multiple(x, n))


def get_multiple(x, n):
    for i in range(1, x):
        if n * i >= x:
            num = n * i
            break
    return num


if __name__ == '__main__':
    get_variables()
