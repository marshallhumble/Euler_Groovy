#!/usr/bin/env python

"""
Number of Ones.
Challenge Description:
Write a program to determine the number of 1 bits in the internal
representation of a given integer.
Input sample:
The first argument will be a path to a filename containing an integer, one per
line. E.g.
10
22
56
Output sample:
Print to stdout, the number of ones in the binary form of each number. E.g.
2
3
3
"""

from sys import argv

in_file = argv[1]


with open(in_file, 'r') as f:
    test_cases = f.read().strip().splitlines()


def check_ones():
    for case in test_cases:
        print(bin(int(case))[2:].count("1"))


if __name__ == '__main__':
    check_ones()
