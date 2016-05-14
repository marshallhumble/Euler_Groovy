#!/usr/bin/env python

"""
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year.
The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday']). Week starts
with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Example:

most_frequent_days(2427) == ['Friday']

most_frequent_days(2185) == ['Saturday']

most_frequent_days(2860) == ['Thursday', 'Friday']


Preconditions: Year is between 1 and 9999. Week starts with Monday.
"""
from datetime import date, timedelta
from collections import Counter
import calendar


def get_days(from_date, to_date):
    delta = timedelta(days=1)
    d = from_date
    days = []
    while d <= to_date:
        days.append(calendar.day_name[d.weekday()])
        d += delta
    return days


def most_frequent_days(cyear):
    count = Counter(get_days(date(cyear, 1, 1), date(cyear, 12, 31)))
    most_common = count.most_common(max(count.values()))
    day_list = []

    for elem in most_common:
        if elem[1] == max(count.values()):
            day_list.append(elem[0])
    # TODO Need to create a sort to return the days in order
    return reversed(day_list)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']

# {'input': 1216, 'answer': ['Friday', 'Saturday']},
# {'input': 1492, 'answer': ['Friday', 'Saturday']},
# {'input': 1770, 'answer': ['Monday']},
# {'input': 1785, 'answer': ['Saturday']},
# {'input': 1, 'answer': ['Monday']},
# {'input': 2135, 'answer': ['Saturday']},
# {'input': 3043, 'answer': ['Sunday']},
# {'input': 2001, 'answer': ['Monday']},
# {'input': 3150, 'answer': ['Sunday']},
# {'input': 3230, 'answer': ['Tuesday']},
# {'input': 328, 'answer': ['Monday', 'Sunday']},
# {'input': 2016, 'answer': ['Friday', 'Saturday']},
# {'input': 334, 'answer': ['Monday']},
# {'input': 1986, 'answer': ['Wednesday']},
# {'input': 3361, 'answer': ['Thursday']},
# {'input': 5863, 'answer': ['Thursday']},
# {'input': 1910, 'answer': ['Saturday']},
# {'input': 1968, 'answer': ['Monday', 'Tuesday']},
# {'input': 7548, 'answer': ['Thursday', 'Friday']},
# {'input': 8116, 'answer': ['Wednesday', 'Thursday']},
# {'input': 9137, 'answer': ['Friday']},
# {'input': 1794, 'answer': ['Wednesday']},
