#!/usr/bin/env python

from sys import argv


def is_prime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


with open(argv[1]) as f:
    lines = f.read().strip().splitlines()


for line in lines:
    print(','.join(str(i) for i in range(2, int(line)) if is_prime(i)))
