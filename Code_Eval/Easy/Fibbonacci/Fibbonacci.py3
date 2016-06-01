#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

fibonacci = [0, 1, 1]

for test in test_cases:
    if test:
        num = int(test)
        if num >= len(fibonacci):
            while len(fibonacci) <= num:
                next = fibonacci[-1] + fibonacci[-2]
                fibonacci.append(next)
        print(fibonacci[num])