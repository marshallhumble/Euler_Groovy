#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(n):
    return sum([i ** 2 for i in range(1, n + 1)])


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


def run_problem():
    return square_of_sum(100) - sum_of_squares(100)


def test_function():
    assert run_problem() == 25164150


if __name__ == '__main__':
    test_function()
