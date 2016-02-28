#!/usr/bin/env python

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (Numbers in text file)
"""

import time

filename = '13_numbers_to_sum.txt'


def get_sol():
    total = sum([int(s.strip()) for s in open(filename).readlines()])
    return int(str(total)[:10])


start = time.time()

print(get_sol())

elapsed = (time.time() - start)
print("\nThis code took: {} seconds".format(str(elapsed)))


#def test_function():
#    assert get_sol() == 5537376230
