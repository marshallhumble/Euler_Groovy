#!/usr/bin/env python

import time

'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (Numbers in text file)
'''

startTime = time.time()

filename = '13_numbers_to_sum.txt'

total = sum([int(s.strip()) for s in open(filename).readlines()])

print(str(total)[:10])

print(time.time() - startTime)