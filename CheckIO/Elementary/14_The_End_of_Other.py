#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is
the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the
result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False

How it is used: Here you can learn about iterating through set type and string data type functions.
"""


def checkio(words_set):
    for word in words_set:
        for suffix in words_set:
            if word != suffix and word.endswith(suffix):
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
def test_function():
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    assert checkio({"longest", "aa", "a"}) == True


if __name__ == '__main__':
    test_function()
