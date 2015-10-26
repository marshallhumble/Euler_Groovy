#!/usr/bin/env python

from sys import argv


def bin_to_dec():
    with open(argv[1], 'r') as f:
        test_cases = f.read().strip().splitlines()
        for i in test_cases:
            print(bin(int(i))[2:])


if __name__ == '__main__':
    bin_to_dec()
