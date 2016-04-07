#!/usr/bin/env python

# Check IO Scientific Expedition/Angles of a Triangle
from math import acos, degrees


def checkio(a, b, c):
    if a + b <= c:
        return [0, 0, 0]
    else:
        angle3 = degrees(acos((a * a + b * b - c * c) / (2.0 * a * b)))
        angle1 = degrees(acos((b * b + c * c - a * a) / (2.0 * b * c)))
        angle2 = degrees(acos((c * c + a * a - b * b) / (2.0 * c * a)))
        return sorted([round(angle1), round(angle2), round(angle3)])


# These "asserts" using only for self-checking and not necessary for auto-testing
def test_function():
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90]
    assert checkio(10, 20, 30) == [0, 0, 0]

if __name__ == '__main__':
    test_function()
