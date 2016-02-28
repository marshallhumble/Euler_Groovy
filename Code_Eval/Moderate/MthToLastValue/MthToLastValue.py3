#!/usr/bin/env python

"""
MTH TO LAST ELEMENT
SPONSORING COMPANY:



CHALLENGE DESCRIPTION:


Write a program which determines the Mth to the last element in a list.

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space delimited characters followed by an
integer. The integer represents an index in the list (1-based), one per line.

For example:

a b c d 4
e f g h 2
OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of
elements in the list, ignore that input.

For example:
a
g

"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

def get_m_value():
    for line in test_cases:
        series, n = line.split()[:-1], int(line.split()[-1])
        if n <= len(series):
            out = series[0 - n]
            print(out)



if __name__ == '__main__':
    get_m_value()