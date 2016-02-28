#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def reverse(file):
    with open(file, 'r') as f:
        for line in nonblank_lines(f):
            revwordorder = ' '.join(word for word in line.split()[::-1])
            print(revwordorder)


def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


if __name__ == '__main__':
    reverse(in_file)
