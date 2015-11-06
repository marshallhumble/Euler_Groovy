#!/usr/bin/env python

"""
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


results = []

for num in range(111,999):
    for x in range(111,999):
        c = num * x
        if str(c) == str(c)[::-1]:
            results.append(c)

print(max(results))


