#!/usr/bin/env python

from datetime import date


def checkio(year):
    day_count = 0
    for month in range(1, 13):
        day = date(year, month, 13)
        # Day = ISO8601 1..7 for Mon -> Sun
        if day.isoweekday() == 5:
            day_count += 1
    return day_count


def test_function():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    assert checkio(2689) == 2, "2689"

if __name__ == "__main__":
    test_function()