#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def capitol_letter(file):
    with open(file, 'r') as f:
        for line in nonblank_lines(f):
            result = ""
            split = line.split()
            for word in split:
                result += word[0].upper() + word[1:] + " "
            print(result.strip())

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


if __name__ == '__main__':
    capitol_letter(in_file)
