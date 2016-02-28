#!/usr/bin/env python

"""
CLEAN UP THE WORDS
CHALLENGE DESCRIPTION:

You have a list of words. Letters of these words are mixed with extra symbols, so it is hard to define the
beginning and end of each word. Write a program that will clean up the words from extra numbers and symbols.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with a list of words: letters are both
lowercase and uppercase, and are mixed with extra symbols.

For example:

(--9Hello----World...--)
Can 0$9 ---you~
13What213are;11you-123+138doing7
OUTPUT SAMPLE:

Print the cleaned up words separated by spaces in lowercase letters.

For example:

hello world
can you
what are you doing
CONSTRAINTS:

Print the words separated by spaces in lowercase letters.
The length of a test case together with extra symbols can be in a range from 10 to 100 symbols.
The number of test cases is 40.
"""

from sys import argv
from re import sub


with open(argv[1], 'r') as f:
    test_case = f.read().strip().splitlines()


def extract_chars(test):
    result = []
    for char in test:
        result.append(' ' if not char.isalpha() else char)
    print(sub(' +', ' ', ''.join(result).lower()).strip())


if __name__ == '__main__':
    for line in test_case:
        extract_chars(line)
