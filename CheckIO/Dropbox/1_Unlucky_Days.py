# !/usr/bin/env python

"""


Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.

Example:

checkio(2015) == 3

checkio(1986) == 1

1

2

Precondition: 1000 < |year| < 3000

"""

from datetime import date


def checkio(year):
    day_count = 0

    for month in range(1, 13):

        day = date(year, month, 13)

        print(day)

        # Day = ISO8601 1..7 for Mon -> Sun

        if day.isoweekday() == 5:
            day_count += 1

    return day_count


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"


if __name__ == '__main__':
    test_function()
