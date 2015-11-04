#!/usr/bin/env python


from sys import argv

coin_values = [1, 3, 5]

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


def count_coins():
    for test in test_cases:
        test = test.rstrip()
        value = int(test)

        total_coin_count = 0
        for coin_value in reversed(coin_values):
            coin_count = value // coin_value
            total_coin_count += coin_count
            value -= coin_count * coin_value
            if value == 0:
                break

        print(total_coin_count)


if __name__ == "__main__":
    count_coins()
