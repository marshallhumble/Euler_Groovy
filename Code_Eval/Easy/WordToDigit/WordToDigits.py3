import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

for test in test_cases:
    print(''.join((str(digits.get(i)) for i in test.split(';'))))