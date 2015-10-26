#!/usr/bin/env python
from sys import argv

in_file = argv[1]


def make_lower(file):
    with open(file, mode='r') as f:
        for line in nonblank_lines(f):
            print(line.lower())


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


if __name__ == '__main__':
    make_lower(in_file)
