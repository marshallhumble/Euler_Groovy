#!/usr/bin/env python

from sys import argv


def open_file(file):
    with open(file, 'r') as f:
        test_cases = f.read().strip().splitlines()
    for line in test_cases:
        n, p1, p2 = [int(num) for num in line.split(',')]
        print(check(n, p1, p2))


def check(n, p1, p2):
    n_binary = bin(n)
    if n_binary[-p1] == n_binary[-p2]:
        return 'true'
    return 'false'


if __name__ == "__main__":
    open_file(argv[1])
