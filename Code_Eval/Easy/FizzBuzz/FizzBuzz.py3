#!/usr/bin/env python
from sys import argv

in_file = argv[1]


def fizz_buzz(file):
    with open(file, mode='r') as f:
        for line in f.readlines():
            game(line)


def game(line):
    num_list = ''
    x, y, n = line.split(' ', 3)
    for _ in range(int(n)):
        num = _ + 1
        if num % int(x) == 0 and num % int(y) == 0:
            num_list += 'FB '
        elif num % int(y) == 0:
            num_list += 'B '
        elif num % int(x) == 0:
            num_list += 'F '
        else:
            num_list += str(num) + ' '
    write_output(num_list)


def write_output(num_list):
    print(num_list.strip())


if __name__ == "__main__":
    fizz_buzz(in_file)
