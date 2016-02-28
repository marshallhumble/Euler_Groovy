#!/usr/bin/env python

# Sieve of Eratosthenes
limit = 8000

primes = [True for n in range(0, limit)]
primes[0], primes[1] = False, False  # 0 and 1 are not primes

for i in range(1, int(limit ** 0.5 + 1)):
    if primes[i]:
        for j in range(i ** 2, limit, i):
            primes[j] = False

index, total = 0, 0
num_primes = 1000

while num_primes:
    if primes[index]:
        total += index
        num_primes -= 1
    index += 1

print(total)
