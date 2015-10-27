#!/usr/bin/env python

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

for test in test_cases:
    integers = [int(i) for i in test.split(',')]
    largest = sum(integers[0:1])
    for i in range(len(integers)):
        for j in range(i + 1, len(integers) + 1):
            sum_pair = sum(integers[i:j])
            largest = sum_pair if sum_pair > largest else largest
    print(largest)