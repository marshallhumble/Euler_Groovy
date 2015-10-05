#!/usr/bin/env python

"""
CountNumbers.py :
Find the numerical value of a word, if it == 100 then place in another file
sort the words by numerical value, then write to a file
"""

from os import path
import sys

__author__ = 'Marshall Humble'

INPUT_FILE = 'american-words'


def dollar_words():
    """
    Assign letters numbers, find those words that == 100
    Then sort them by smallest to largest, print to console
    """
    if not path.isfile(INPUT_FILE):
        sys.exit("Input not found, exiting.")
    else:
        word_list = list()
        with open(INPUT_FILE, 'r') as content_file:
            for i in content_file:
                i = i.strip('\n')
                if sum(ord(l) - 96 for l in i.lower().rstrip()) == 100:
                    word_list.append(i)
            print(*(sorted(word_list, key=len)), sep='\n')
            # Uncommment below to make the above line work in Python 2:
            # word_list = (sorted(word_list, key=len))
            # for p in word_list:
            #    print(p)
        content_file.close()


if __name__ == "__main__":
    dollar_words()
