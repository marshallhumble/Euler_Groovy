#!/usr/bin/env python

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


def convert_time():
    for line in test_cases:
        out = ' '.join(sorted(line.split(), reverse=True))
        print(out)


if __name__ == '__main__':
    convert_time()
