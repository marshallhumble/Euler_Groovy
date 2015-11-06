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

import time
import math

start = time.time()

def dickson_method(s,t):
    """
    Use Dickson's Method to generate x,y,z for Pythagorean triples r^2 = 2st then:
    x = r + s, y = r + t, z = r + s + t
    """
    r = 2 * (s*t)
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
            print(x*y*z)


elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")
