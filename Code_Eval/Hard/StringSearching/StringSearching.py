#!/usr/bin/env python

"""
String Searching

Challenge Description:

You are given two strings. Determine if the second string is a substring of the first (Do NOT use any substr type
library function). The second string may contain an asterisk(*) which should be treated as a regular expression i.e.
matches zero or more characters. The asterisk can be escaped by a \ char in which case it should be interpreted as a
regular '*' character. To summarize: the strings can contain alphabets, numbers, * and \ characters.
Input sample:

Your program should accept as its first argument a path to a filename. The input file contains two comma delimited
strings per line. E.g.

Hello,ell
This is good, is
CodeEval,C*Eval
Old,Young

Output sample:

If the second string is indeed a substring of the first, print out a 'true'(lowercase), else print out a
'false'(lowercase), one per line. E.g.

true
true
true
false


"""

import sys


def is_substring(a, b):
    a = a.replace("*", "@")
    b = b.replace("\\*", "@")

    for e in b.split("*"):
        pos = a.find(e)
        if pos < 0:
            return False
        a = a[pos + len(e):]
    return True


def main():
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            a, b = line.rstrip().split(",")
            print(str(is_substring(a, b)).lower())


if __name__ == "__main__":
    main()
