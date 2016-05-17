#!/usr/bin/env python

from sys import argv


with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


for line in test_cases:
    x, y = map(str, line.split(','))
    if x[-(len(y)):] == y:
        print('1')
    else:
        print('0')