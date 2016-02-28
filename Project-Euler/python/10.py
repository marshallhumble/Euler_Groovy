#!/usr/bin/env python

import time

start = time.time()

"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def primes_sieve(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True

    for i in primes:
        factors = range(i, limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i] == True]


print(sum(primes_sieve(2000000)))


def sum_primes(x):
    return sum(primes_sieve(x))


def test_function():
    assert sum_primes(2000000) == 142913828922
