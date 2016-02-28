#!/usr/bin/env python

from sys import argv


with open(argv[1], 'r') as f:
    cases = f.read().strip().splitlines()

for item in cases:
    text, letters = item.split(',')
    text = text.split()
    for c in letters:
        for t in text:
            text[text.index(t)] = t.replace(c, '')
    print(' '.join(text))
