import os
import re
print("day10")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

data = sorted([0] + [int(x) for x in open(path).readlines()])
next =data[1:] + [data[-1]+3]
diff = [y-x for x,y in zip(data, next)]
print(f"first mission {diff.count(1)*diff.count(3)}")

mult = {data[-1] : 1}
for val in reversed(data[0:-1]):
    ret = 0
    for step in range(1,4):
        if val+step in mult:
            # print(f"found {val+step} ")
            ret += mult[val+step]
    mult[val] = ret

print(f"ways {mult[0]} ")
assert 7086739046912 == mult[0]
