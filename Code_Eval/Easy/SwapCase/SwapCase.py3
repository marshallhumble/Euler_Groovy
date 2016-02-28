#!/usr/bin/env python

"""
Write a program which swaps letters' case in a sentence. All non-letter characters should remain the same.

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

Hello world!
JavaScript language 1.8
A letter
OUTPUT SAMPLE:

Print results in the following way.

hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER
"""

from sys import argv


in_file = argv[1]


def change_case():
    with open(in_file, 'r') as f:
        for line in f:
            print(line.swapcase())


if __name__ == '__main__':
    change_case()
