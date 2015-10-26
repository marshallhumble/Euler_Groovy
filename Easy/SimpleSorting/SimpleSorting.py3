#!/usr/bin/env python

from sys import argv

in_file = argv[1]


def simple_sort(file):
    with open(file, 'r') as myfile:
        for line in myfile:
            slist = (sorted(map(float, line.split(' '))))
            answer = ' '.join(map(str, slist))
            print(answer.strip())


if __name__ == '__main__':
    simple_sort(in_file)
