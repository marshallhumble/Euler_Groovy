#!/usr/bin/env python

"""
Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496
OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19
"""

from sys import argv

in_file = argv[1]


def sum_line():
    with open(in_file, 'r') as f:
        for line in f:
            test_cases = map(int, line.strip())
            print(sum((int(i) for i in test_cases)))


if __name__ == '__main__':
    sum_line()
