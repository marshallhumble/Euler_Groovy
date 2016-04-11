import datetime
from datetime import date

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    d1 = date.strftime(date1, '%Y, %b, %d')
    d2 = date.strftime(date2, '%Y, %m, %d')
    d3 = d1 - d2
    print(d3)
    print('f')

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    days_diff((1982, 4, 19), (1982, 4, 22))
