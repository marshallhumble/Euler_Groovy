# CodeWars Kata/Digital Root


def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        return digital_root(digit_sum(n))


def digit_sum(num):
    return sum([int(char) for char in str(num)])


