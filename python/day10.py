import os
import re
import copy
print("day10")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

data = [int(x) for x in open(path).readlines()]
print(data)
data.append(0)
d = sorted(data)

print(data)

print(d)
next =d[1:]
print(next)
next.append(next[-1]+3)

table = zip(d, next)
print(table)
global diff
diff = [y-x for x,y in table]
print(diff)
print(diff.count(1))
print(diff.count(3))
print(diff.count(1)*diff.count(3))

valid = []
def nextStep(output, index):
    global diff
    # print (output)
    if index >= len(diff):
        # print(f"miss")
        return
        
    if output[-1] < d[index]-3:
        # print(f"to big {output[-1]} {d[index]}")
        return
    output.append(d[index])
    if output[-1] == d[-1]:
        valid.append(output)
        return
    for step in range(1,4):
        bbbbb= copy.deepcopy(output)
        nextStep(bbbbb, index+step)

hhh = nextStep([0],1)
for x in valid:
    print(x)
#print(valid)
print(len(valid))
