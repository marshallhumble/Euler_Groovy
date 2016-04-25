#!/usr/bin/env python

"""
Write a program which finds the next-to-last word in a string.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

some line with text
another line
Each line has more than one word.

OUTPUT SAMPLE:

Print the next-to-last word in the following way.

with
another
"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


def check_lines(line):
    return line.split()[-2]


for test in test_cases:
    print(check_lines(test))

