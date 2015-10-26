#!/usr/bin/env python

from math import sqrt

def sum_primes(limit):
    sieve = range(limit+1); sieve[1] = 0
    for n in range(2, int(sqrt(limit))+1):
        if sieve[n] > 0:
            for i in range(n*n, limit+1, n): sieve[i] = 0
    return sum(sieve)

if __name__ == '__main__':
    sum_primes(1000)