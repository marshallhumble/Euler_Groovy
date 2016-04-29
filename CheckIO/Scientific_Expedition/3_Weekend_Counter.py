#!/usr/bin/env python

"""
Sofia has given you a schedule and two dates and told you she needs help planning her weekends. She has asked you to
count each day of rest (Saturday and Sunday) starting from the initial date to final date. You should count the initial
and final dates if they fall on a Saturday or Sunday.

The dates are given as datetime.date (Read about this module here). The result is an integer.

Input: Start and end date as datetime.date.

Output: The quantity of the rest days as an integer.

Example:

checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8
checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2

How it is used: Now is a good time to learn how to work with dates. These ideas here often come up in calendar apps,
customer relation management software, automated messaging schedulers among many other things.

Precondition: start_date < end_date.
"""

from datetime import date, timedelta


def checkio(from_date, to_date):
    delta = timedelta(days=1)
    d = from_date
    diff = 0
    weekend = {6, 7}
    while d <= to_date:
        if d.isoweekday() in weekend:
            diff += 1
        d += delta
    return diff


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
