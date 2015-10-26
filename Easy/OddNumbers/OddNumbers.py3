#!/usr/bin/env python


def primes():
    for num in range(0, 100):
        if not num % 2 == 0:
            print(num)


if __name__ == '__main__':
    primes()
