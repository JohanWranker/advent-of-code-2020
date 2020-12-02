import os
import re
print("day02")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

successful = 0
with open(path) as file:
    for line in file:
        # print(line)
        m = re.match(r'(?P<low>\d+)-(?P<high>\d+)\s+(?P<char>\w):\s+(?P<data>\w+)', line)
        if m is None:
            continue
        number = m.group('data').count(m.group('char'))
        if number >= int(m.group('low')) and number <= int(m.group('high')):
            successful +=1

print(successful)

number = 0
with open(path) as file:
    for line in file:
        m = re.match(r'(?P<pos1>\d+)-(?P<pos2>\d+)\s+(?P<char>\w):\s+(?P<data>\w+)', line)
        data = m.group('data')
        if [ data[int(m.group('pos1'))-1], data[int(m.group('pos2'))-1]].count(m.group('char')) == 1:
            number += 1
        print(number)






