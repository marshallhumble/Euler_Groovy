#!/usr/bin/env python

"""
DELTA TIME
CHALLENGE DESCRIPTION:

You are given the pairs of time values. The values are in the HH:MM:SS format with leading zeros.
Your task is to find out the time difference between the pairs.

INPUT SAMPLE:

The first argument is a file that contains lines with the time pairs.

For example:

14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56
OUTPUT SAMPLE:

Print to stdout the time difference for each pair, one per line. You must format the time values in HH:MM:SS
with leading zeros.

For example:

01:14:46
09:06:33
00:30:22
20:45:08
00:15:11


"""

from sys import argv
from datetime import datetime

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

for test in test_cases:
    x, y = test.split(' ')
    dt1 = datetime.strptime(x, '%H:%M:%S')
    dt2 = datetime.strptime(y, '%H:%M:%S')
    dtdiff = dt1 - dt2
    z = abs(dtdiff)
    final = datetime.strptime(str(z), '%H:%M:%S')
    print(str(final)[11:])
