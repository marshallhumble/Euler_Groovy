#!/usr/bin/env python

"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True,
then return True only if both are negative.

pos_neg(1, -1, False) == True
pos_neg(-1, 1, False) == True
pos_neg(-4, -5, True) == True
"""


def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False

    elif not negative:
        if a < 0 and b > 0:
            return True
        elif a > 0 and b < 0:
            return True
        else:
            return False



def test_function():
    assert pos_neg(1, -1, False) == True
    assert pos_neg(-1, 1, False) == True
    assert pos_neg(-4, -5, True) == True
    assert pos_neg(-4, -5, False) == False
    assert pos_neg(-4, 5, False) == True
    assert pos_neg(-4, 5, True) == False
    assert pos_neg(1, 1, False) == False
    assert pos_neg(-1, -1, False) == False
    assert pos_neg(1, -1, True) == False
    assert pos_neg(-1, 1, True) == False
    assert pos_neg(1, 1, True) == False
    assert pos_neg(-1, -1, True) == True
    assert pos_neg(5, -5, False) == True
    assert pos_neg(-6, 6, False) == True
    assert pos_neg(-5, -6, False) == False
    assert pos_neg(-2, -1, False) == False
    assert pos_neg(1, 2, False) == False
    assert pos_neg(-5, 6, True) == False
    assert pos_neg(-5, -5, True) == True


if __name__ == '__main__':
    test_function()
