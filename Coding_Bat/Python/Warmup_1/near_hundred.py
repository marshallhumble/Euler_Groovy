#!/usr/bin/env python

"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) == True
near_hundred(90) == True
near_hundred(89) == False
"""


def near_hundred(n):
    return 190 <= abs(n) <= 210 or 90 <= abs(n) <= 110


def test_function():
    assert near_hundred(93) == True
    assert near_hundred(90) == True
    assert near_hundred(89) == False
    assert near_hundred(110) == True
    assert near_hundred(111) == False
    assert near_hundred(121) == False
    assert near_hundred(0) == False
    assert near_hundred(5) == False
    assert near_hundred(191) == True
    assert near_hundred(189) == False
    assert near_hundred(190) == True
    assert near_hundred(200) == True
    assert near_hundred(210) == True
    assert near_hundred(211) == False
    assert near_hundred(290) == False


if __name__ == '__main__':
    test_function()
