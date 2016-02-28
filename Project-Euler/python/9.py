#!/usr/bin/env python

"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math


def dickson_method(s, t):
    """
    Use Dickson's Method to generate x,y,z for Pythagorean triples r^2 = 2st then:
    x = r + s, y = r + t, z = r + s + t
    """
    r = 2 * (s * t)
    r = math.sqrt(r)
    x = r + s
    y = r + t
    z = r + s + t
    return x, y, z


for i in range(1, 999):
    """
    We know x,y,z are < 1000
    """
    for x in range(1, 999):
        while sum(dickson_method(i, x)) == 1000:
            print(dickson_method(i, x))
            x, y, z = dickson_method(i, x)
            print(x * y * z)


def sum_method(i, x):
    x, y, z = dickson_method(i, x)
    return x * y * z


def test_function():
    assert dickson_method(50, 225) == (200.0, 375.0, 425.0)
    assert dickson_method(225, 50) == (375.0, 200.0, 425.0)
    assert sum_method(50, 225) == 31875000.0
    assert sum_method(225, 50) == 31875000.0
