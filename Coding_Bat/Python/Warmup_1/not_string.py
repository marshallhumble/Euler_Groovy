#!/usr/bin/env python

"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with
 "not", return the string unchanged.

not_string('candy') == 'not candy'
not_string('x') == 'not x'
not_string('not bad') == 'not bad'
"""


def not_string(str):
    if str[0:3] == 'not':
        return str
    else:
        return 'not ' + str


def test_function():
    assert not_string('candy') == 'not candy'
    assert not_string('x') == 'not x'
    assert not_string('not bad') == 'not bad'
    assert not_string('bad') == 'not bad'
    assert not_string('not') == 'not'
    assert not_string('is not') == 'not is not'
    assert not_string('no') == 'not no'


if __name__ == '__main__':
    test_function()
