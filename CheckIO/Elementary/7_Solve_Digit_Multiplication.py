#!/usr/bin/env python

"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.


"""

from functools import reduce

checkio = lambda number: reduce(lambda res, x: res * x, [int(num) for num in str(number) if int(num)], 1)


def test_function():
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1


if __name__ == '__main__':
    test_function()
