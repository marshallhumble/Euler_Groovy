#!/usr/bin/env python

from math import sqrt

"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def counter():
    count_prime = 0
    prime = 1
    count_token = 2

    def prime_check(num):
        prime = True
        for i in range(int(sqrt(num))):
            i += 2
            if num % i == 0:
                prime = False
                break
        if num == 2:
            return True
        else:
            return prime

    while count_prime < 10001:
        if prime_check(count_token):
            count_prime += 1
            prime = count_token
        count_token += 1
    print("The 10001'st Prime number is: ", prime)

if __name__ == '__main__':
    counter()
