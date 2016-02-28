#!/usr/bin/env python

import time

start = time.time()

'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatz_sequence(x):
    seq = [x]
    if x < 1:
        return []
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        seq.append(x)  # Added line
    return seq

comparator = 1
largest_num = 0

for i in range(500, 1000000):
    seq_num = collatz_sequence(i)
    if len(seq_num) > comparator:
        comparator = len(seq_num)
        largest_num = i
        print(largest_num)
        print(seq_num)

elapsed = (time.time() - start)
print("\nThis code took: {} seconds".format(str(elapsed)))
