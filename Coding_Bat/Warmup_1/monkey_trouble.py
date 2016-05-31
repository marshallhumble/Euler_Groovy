#!/usr/bin/env python

"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if
they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""


def monkey_trouble(a_smile, b_smile):
    if not a_smile and not b_smile:
        return True
    elif a_smile and b_smile:
        return True
    else:
        return False


def test_function():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True
    assert monkey_trouble(True, False) == False
    assert monkey_trouble(False, True) == False


if __name__ == '__main__':
    test_function()
