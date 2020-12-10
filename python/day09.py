import os
import re
import copy
print("day09")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

data = [int(x) for x in open(path).readlines()]
# print(data)

preamble = 25
expected = 0
for index in range(preamble, len(data)):
    expected = data[index]
    found = False
    for outer in range(-1, -preamble-1, -1):
        for inner in range(outer-1, -preamble-1, -1):
            if data[index] == data[index+outer] + data[index+inner]:
                # print(f"Found")
                found = True
                break
        if found:
            break
    if not found:
        print(f"On pos {index}+1 is not found {expected}")
        break

for index in range(0, len(data)):
    sum = data[index]
    offset = 0
    while (sum < expected):
        offset +=1
        sum += data[index+offset]
        # print(f"{sum}")
    if sum == expected:
        v1 = min(data[index:index+offset])
        v2 = max(data[index:index+offset])
        print(f"foundit {index} {index+offset} {v1 +v2}")
        break
