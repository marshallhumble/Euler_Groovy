#!/usr/bin/env python


"""
Calculate Distance.
Challenge Description:
You have coordinates of 2 points and need to find the distance between them.
Input sample:
Your program should accept as its first argument a path to a filename. Input
example is the following
(25, 4) (1, -6)
(47, 43) (-25, -11)
All numbers in input are integers between -100 and 100.
Output sample:
Print results in the following way.
26
90
You don't need to round the results you receive.
They must be integer numbers between -100 and 100.
"""

from sys import argv
from math import hypot

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

for test in test_cases:
    nums = [int(i) for i in
            test.replace(',', '').replace('(', '').replace(')', '').split()]
    print(int(hypot(nums[0] - nums[2], nums[1] - nums[3])))
