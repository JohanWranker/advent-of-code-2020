import os
import re
import copy
print("day09")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

data = [int(x) for x in open(path).readlines()]
print(data)

lastOk = True
preamble = 25
for index in range(preamble, len(data)):
    expected = data[index]
    found = False
    for outer in range(-1, -preamble-1, -1):
        for inner in range(outer-1, -preamble-1, -1):
            pos1 = index+outer
            pos2 = index+inner
            # print (f"{pos1} + {pos2}")
            # print (f"{data[pos1] + data[pos2]} == {data[pos1]} + {data[pos2]}")
            if data[index] == data[pos1] + data[pos2]:
                print(f"Found")
                found = True
                break
        if found:
            break
    if not found:
        print(f"On pos {index}+1 is not found {expected}")
        exit(0)


        #2089807806
