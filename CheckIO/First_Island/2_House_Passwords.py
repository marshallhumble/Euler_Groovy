#!/usr/bin/env python

import re

"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password
security check module. The password will be considered strong enough if its length is greater than or equal to
10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The
password contains only ASCII latin letters or digits.
Input: A password as a string (Unicode for python 2.7).
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
In the results you will see the converted results.

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""


def checkio(data):
    upper_let = 0
    digit_let = 0
    let_low = 0

    if len(data) < 10:
        return False

    for let in data:
        if let.isupper():
            upper_let += 1
        if let.isdigit():
            digit_let += 1
        if let.islower():
            let_low += 1

    if upper_let >= 1 and digit_let >= 1 and let_low >= 1:
        return True
    else:
        return False


def test_function():
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"


if __name__ == '__main__':
    test_function()

"""
Regex Solution:

import re
​
def checkio(data):
    return len(data)>9 and len(data) <= 64 and re.search("[a-z]+", data) and re.search("[A-Z]+", data) and re.search("[0-9]+", data) and re.search("[a-zA-Z0-9]+", data)
"""
