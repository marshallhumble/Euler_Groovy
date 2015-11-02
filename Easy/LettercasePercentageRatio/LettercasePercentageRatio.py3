#!/usr/bin/env python

"""
LETTERCASE PERCENTAGE RATIO
CHALLENGE DESCRIPTION:


Your task is to write a program which determines (calculates)
the percentage ratio of lowercase and uppercase letters.

INPUT SAMPLE:

Your program should accept a file as its first argument. Each line of input contains
a string with uppercase and lowercase letters.

For example:

thisTHIS
AAbbCCDDEE
N
UkJ
OUTPUT SAMPLE:

For each line of input, print the percentage ratio of uppercase and lowercase letters
rounded to the second digit afterthe point.

For example:

lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67

"""

from sys import argv
from string import ascii_lowercase, ascii_uppercase

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

for line in test_cases:
    length = len(line)
    lower = (sum(1 for l in line if l in ascii_lowercase) * 100.0) / length
    upper = (sum(1 for u in line if u in ascii_uppercase) * 100.0) / length
    print("lowercase: {0:.2f} uppercase: {1:.2f}".format(lower, upper))
