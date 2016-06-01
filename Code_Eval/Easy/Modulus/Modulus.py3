#!/usr/bin/env python

"""
Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

20,6
2,3
You may assume M will never be zero.

OUTPUT SAMPLE:

Print out the value of N Mod M
"""

from sys import argv


in_file = argv[1]


def find_mod(a, b):
    x = a / b
    y = int(x) * b
    return a - y


def read_file(file):
    with open(file, 'r') as f:
        lines = f.read().strip().splitlines()
        for _ in lines:
            x, y = (int(i) for i in _.split(','))
            print(find_mod(x, y))

read_file(in_file)
