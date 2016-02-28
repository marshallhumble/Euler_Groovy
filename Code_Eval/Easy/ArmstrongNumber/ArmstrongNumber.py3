#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def is_armstrong_number(test):
    print(sum(pow(int(i), len(test)) for i in test) == int(test))


def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            is_armstrong_number(line.strip())

if __name__ == '__main__':
    read_file(in_file)
