#!/usr/bin/env python

"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n
is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""


def diff21(n):
    if n <= 21:
        return abs(n - 21)
    else:
        return abs(2 * (n - 21))


def test_function():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(25) == 8
    assert diff21(30) == 18
    assert diff21(0) == 21
    assert diff21(1) == 20
    assert diff21(2) == 19
    assert diff21(-1) == 22
    assert diff21(-2) == 23
    assert diff21(50) == 58


if __name__ == '__main__':
    test_function()
