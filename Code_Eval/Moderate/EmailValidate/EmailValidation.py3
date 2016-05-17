#!/usr/bin/env python

"""
EMAIL VALIDATION
CHALLENGE DESCRIPTION:

You are given several strings that may/may not be valid emails. You should write a regular expression that determines
 if the email id is a valid email id or not. You may assume all characters are from the english language.

INPUT SAMPLE:

Your program should accept as its first argument a filename. This file will contain several text strings, one per line.
Ignore all empty lines. E.g.

foo@bar.com
this is not an email id
admin#codeeval.com
good123@bad.com
OUTPUT SAMPLE:

Print out 'true' (all lowercase) if the string is a valid email. Else print out 'false' (all lowercase). E.g.

true
false
false
true
"""

from sys import argv
import re


def validate_emaill(file):
    with open(file, 'r') as f:
        for line in nonblank_lines(f):
            if line:
                email_regex = re.compile(
                    '^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[' \
                    'a-z|0-9|-]{2,}')
                print({None: 'false'}.get(re.match(email_regex, line), 'true'))



def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line


if __name__ == '__main__':
    validate_emaill(argv[1])