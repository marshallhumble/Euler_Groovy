
filename = '13_numbers_to_sum.txt'

total = sum([int(s.strip()) for s in open(filename).readlines()])

print(str(total)[:10])