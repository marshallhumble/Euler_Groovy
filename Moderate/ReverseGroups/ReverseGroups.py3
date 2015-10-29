#!/usr/bin/env python

"""

"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

for test in test_cases:
    nums_as_str, interval_as_str = test.split(';')
    lst, interval = nums_as_str.split(','), int(interval_as_str)
    last = (len(lst) - (len(lst) % interval)) - 1
    if interval != 1:
        for i in range(0, last, interval):
            lst[i:i + interval] = lst[i:i + interval][::-1]
    print(','.join(lst))