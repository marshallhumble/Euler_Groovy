#!/usr/bin/env python

"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""


def sleep_in(weekday, vacation):
    if vacation:
        return True
    elif weekday and vacation == False:
        return False
    else:
        return True


def test_function():
    assert sleep_in(False, False) == True, "Should return True"
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True
    assert sleep_in(True, True) == True

if __name__ == '__main__':
    test_function()