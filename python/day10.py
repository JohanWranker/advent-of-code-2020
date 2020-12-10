import os
import re
import copy
print("day10")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

data = [int(x) for x in open(path).readlines()]
data.append(0)
d = sorted(data)

next =d[1:]
print(next)
next.append(next[-1]+3)

table = zip(d, next)
print(table)

global diff
diff = [y-x for x,y in table]
print(f"first mission {diff.count(1)*diff.count(3)}")

count = 0
def wayto22(val):
    ret = 0
    if val == d[-1]:
        return 1
    for step in range(1,4):
        if val+step in d:
            ret += wayto22(val+step)
    return ret
    
# r = wayto22(0)

mult = {d[-1] : 1}
# multi = 1

for val in reversed(d[0:-1]):
    ret = 0
    for step in range(1,4):
        if val+step in mult:
            print(f"found {val+step} ")
            ret += mult[val+step]
            
            # print(f"found {val+step} {ret} {mult}")
            # exit(0)
    mult[val] = ret

print(d)
print(f"ways {mult} ")

print(f"ways {multi} ")
