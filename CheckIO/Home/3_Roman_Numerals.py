#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which
 are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are
based on combinations of these seven symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.
For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000
"""
from collections import OrderedDict


def checkio(data):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(data):
        for r in roman.keys():
            x, y = divmod(data, r)
            yield roman[r] * x
            data -= (r * x)
            if data > 0:
                roman_num(data)
            else:
                break

    return "".join([a for a in roman_num(data)])


def test_function():
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'


if __name__ == '__main__':
    test_function()
