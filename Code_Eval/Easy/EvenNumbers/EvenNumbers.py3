#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def check_even(num):
    if num % 2 == 0:
        print('1')
    else:
        print('0')


def file_read():
    with open(in_file, 'r') as f:
        for line in f:
            check_even(float(line))


if __name__ == '__main__':
    file_read()
