#!/usr/bin/env python

MY_LIST = []

def palindrome():
    max_num = 1000
    for num in range(0, max_num):
        if str(num) == str(num)[::-1]:
            find_prime(num)


def find_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            add_list(num)

def add_list(num):
    MY_LIST.append(num)


if __name__ == '__main__':
    palindrome()
    print(MY_LIST[-1])