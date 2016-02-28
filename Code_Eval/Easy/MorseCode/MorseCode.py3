#!/usr/bin/env python

"""

"""

from sys import argv, stdout

with open(argv[1], 'r') as f:
    test_cases = f.read().strip().splitlines()

code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

morse_code = dict(zip(code.values(), code.keys()))


for line in test_cases:
    if ' ' == line:
        continue
    for morse in line.split(' '):
        if morse == '':
            stdout.write(' ')
        else:
            stdout.write(morse_code[morse])
    stdout.write("\n")
