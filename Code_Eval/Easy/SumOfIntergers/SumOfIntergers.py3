#!/usr/bin/env python

from sys import argv

in_file = argv[1]


print(sum([int(s.strip()) for s in open(in_file).readlines()]))
