#!/usr/bin/env python

"""


215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""


def solve_fifteen():
    return sum(int(x) for x in str(2 ** 1000))


def test_function():
    assert solve_fifteen() == 1366

if __name__ == '__main__':
    test_function()
