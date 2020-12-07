import os
import re
print("day06")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

bagTable = {}

groups = [x.split("\n") for x in open(path).read().split("\n\n")]
print(groups)

def addTuples(tt):
    tup = []
    # print(tt)
    m = re.match(r"(\d)\s(.*?),\s(.*)", tt)
    if m is not None:
        # print(m.groups())
        tup = addTuples(m.group(3))
    else:
        #bag1 = m.group(2) if m.group(2)[-1]!= 's' else m.group(2)[:-1]
        #tup = (bag1, int(m.group(1)))
        #print (tup)           
        #list = addTuples(m.group(3))
        #exit(1)
        m = re.match(r"(\d)\s(.*).", tt)
    # print (m.groups())
    bag1 = m.group(2) if m.group(2)[-1]!= 's' else m.group(2)[:-1]
    tup.append((bag1, int(m.group(1))))
    return tup

for group in groups:
    pass
    # print(f"length of group {len(group)} content {group}")
    for g in group:
        print(f"content {g}")
        m = re.match(r"(.*)s\scontain\s((\d).*)", g)
        if m is not None:
            # print("multiple")
            # print(m.groups())
            bagTable[m.group(1)] = addTuples( m.group(2))
            # print (bagTable)
            continue
        m = re.match(r"(.*)s\scontain\s(no)\s(.*).", g)
        if m is not None:# No bag
            bagTable[m.group(1)] = []
        elif g == "":
            pass
        else:
            print 
            assert False


def bagContainsShine(bag, depth):
    found = False
    # print(f" ##{bag}##")
    bag = bag.strip()
    if not bag in bagTable:
        bag = bag[:-1]
    assert (bag in bagTable), f"'{bag}' not found"
    
    for bb in bagTable[bag]:
        # print("   "*depth + bb[0])
        if bag == 'shiny gold bag':
            # print("   "*depth + "FOUND")
            found = True
        found = found or bagContainsShine(bb[0], depth +1)
    return found

# print (bagTable)
# print (bagTable)
count = 0
for bag in bagTable:
    if bagContainsShine(bag, 0):
        count += 1
print(count)
