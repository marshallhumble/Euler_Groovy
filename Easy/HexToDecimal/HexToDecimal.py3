#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def hex_to_decimal(file):
    with open(file, 'r') as f:
        for line in nonblank_lines(f):
            x = int(line, 16)
            print(x)


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


if __name__ == '__main__':
    hex_to_decimal(in_file)
