#!/usr/bin/env python

"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) == 3
sum_double(3, 2) == 5
sum_double(2, 2) == 8
"""


def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


def test_function():
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8
    assert sum_double(-1, 0) == -1
    assert sum_double(3, 3) == 12
    assert sum_double(0, 0) == 0
    assert sum_double(0, 1) == 1
    assert sum_double(3, 4) == 7


if __name__ == '__main__':
    test_function()
