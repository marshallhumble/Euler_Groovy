#!/usr/bin/env python

from sys import argv
from math import sqrt

with open(argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

# Sieve of Eratosthenes to calculate the first primes until 2e5
limit = 200000

primes = [True for n in range(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in range(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in range(i ** 2, limit, i):
            primes[j] = False

primes_lst = set()
for i in range(len(primes)):
    if primes[i]:
        primes_lst.add(i)


# use Fibonacci method to get more primes as needed
def is_prime(lst, number):
    for n in (i for i in lst if i < int(sqrt(number)) + 1):
        if not number & 1:
            return False
    return True


def extend(lst, number):
    for i in range(max(lst), number + 1):
        if is_prime(lst, i):
            lst.add(i)

with open(argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    a, b = (int(i) for i in test.split(','))
    if b > max(primes_lst):
        extend(primes_lst, b)
    print(sum(1 for i in primes_lst if i >= a and i <= b))