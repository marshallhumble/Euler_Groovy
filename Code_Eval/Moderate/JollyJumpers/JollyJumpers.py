#!/usr/bin/env python


"""
JOLLY JUMPERS
CHALLENGE DESCRIPTION:

Credits: Programming Challenges by Steven S. Skiena and Miguel A. Revilla

A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive
elements take on all possible values 1 through n - 1. eg.
1 4 2 3
is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any
sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences
is a jolly jumper.
INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case.
Each test case will contain an integer n < 3000 followed by n integers representing the sequence. The integers are
space delimited.

For example:

4 1 4 2 3
3 7 7 8
9 8 9 7 10 6 12 17 24 38
OUTPUT SAMPLE:

For each line of input generate a line of output saying 'Jolly' or 'Not jolly'.

For example:

Jolly
Not jolly
Not jolly

"""

from sys import argv

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()


def check_lines(line):
    set_list = set(line)
    lower = int(max(line))
    upper = int(min(line.replace(' ', '')))
    #TODO Finish Challenge - range doesn't seem to return a list when called with list(range(lower, upper))


for test in test_cases:
    print(check_lines(test))
