#!/usr/bin/env python

"""
UNIQUE ELEMENTS
CHALLENGE DESCRIPTION:


You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

INPUT SAMPLE:

File containing a list of sorted integers, comma delimited, one per line. E.g.

1,1,1,2,2,3,3,4,4
2,3,4,5,5
OUTPUT SAMPLE:

Print out the sorted list with duplicates removed, one per line.
E.g.

1,2,3,4
2,3,4,5
SUBMIT
"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

def convert_list():
    for test in test_cases:
        line = sorted(set([int(i) for i in test.split(',')]))
        print(','.join((str(j) for j in line)))


if __name__ == '__main__':
    convert_list()