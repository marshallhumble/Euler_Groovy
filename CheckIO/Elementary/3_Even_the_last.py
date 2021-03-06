#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
then multiply this summed number and the final element of the array together. Don't forget that the first element
has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.
Precondition: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""


def checkio(array):
    if isinstance(array, int):
        return array ** array
    elif len(array) == 0:
        return 0
    else:
        mult = array[-1]
        answ = 0
        for num in array[::2]:
            answ += num
        return answ * mult


def test_function():
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"


if __name__ == '__main__':
    test_function()
