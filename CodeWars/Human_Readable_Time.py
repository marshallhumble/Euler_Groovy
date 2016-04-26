#!/usr/bin/env python

"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a
human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

Smallest code on Kata was:   return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

"""
import time


def make_readable(seconds):
    if seconds == 0:
        return "00:00:00"
    elif seconds <= 86399:
        return time.strftime('%H:%M:%S', time.gmtime(seconds))
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)


def test_function():
    assert make_readable(0) == "00:00:00"
    assert make_readable(5) == "00:00:05"
    assert make_readable(60) == "00:01:00"
    assert make_readable(86399) == "23:59:59"
    assert make_readable(359999) == "99:59:59"

if __name__ == '__main__':
    test_function()
