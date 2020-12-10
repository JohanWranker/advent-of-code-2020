import os
import re
from datetime import datetime
import time

print("day10")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)
rawtext = open(path).readlines()

# Get all joltage all inital 0 and sort it
data = sorted([0] + [int(x) for x in rawtext])
# List with "next" joltage - include output which is last +3
next =data[1:] + [data[-1]+3]
# Make a difflist
diff = [y-x for x,y in zip(data, next)]
print(f"first mission {diff.count(1)*diff.count(3)}")
assert 2210 == diff.count(1)*diff.count(3)

#dict over the paths to the device, add the last jolt which has 1 exit path
paths = {data[-1] : 1}
for val in reversed(data[0:-1]):
    # handle the jolts starting at the last-but-one
    paths[val] = 0
    # Test each jolt with offset 1-3
    for step in [1,2,3]:
        if val+step in paths:
            # New path found, add based on the number of way "next step" has 
            paths[val] += paths[val+step]
print(f"ways {paths[0]} ")
assert 7086739046912 == paths[0]
