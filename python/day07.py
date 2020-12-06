import os
import re
print("day06")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)



groups = [x.split("\n") for x in open(path).read().split("\n\n")]
print(groups)
#for group in groups:
#    pass
#    print(f"length of group {len(group)} content {group}")

