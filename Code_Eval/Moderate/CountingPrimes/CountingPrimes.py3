#!/usr/bin/env python

"""
COUNTING PRIMES
CHALLENGE DESCRIPTION:


Given two integers N and M, count the number of prime numbers between N and M (both inclusive)

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma
separated positive integers. E.g.

2,10
20,30
OUTPUT SAMPLE:

Print out the number of primes between N and M (both inclusive)

4
2
SUBMIT SOLUTION
"""

from sys import argv
from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


with open(argv[1]) as f:
    lines = f.read().strip().splitlines()

for line in lines:
    count = 0
    start, end = map(int, line.split(','))
    for n in range(start, end):
        if is_prime(n):
            count += 1
        else:
            continue
    print(count)
