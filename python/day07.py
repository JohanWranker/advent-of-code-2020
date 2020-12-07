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
    m = re.match(r"(\d)\s(.*?),\s(.*)", tt)
    if m is not None:
        tup = addTuples(m.group(3))
    else:
        m = re.match(r"(\d)\s(.*).", tt)
    bag1 = m.group(2) if m.group(2)[-1]!= 's' else m.group(2)[:-1]
    tup.append((bag1, int(m.group(1))))
    return tup

for group in groups:
    pass
    for g in group:
        print(f"content {g}")
        m = re.match(r"(.*)s\scontain\s((\d).*)", g)
        if m is not None:
            bagTable[m.group(1)] = addTuples( m.group(2))
            continue
        m = re.match(r"(.*)s\scontain\s(no)\s(.*).", g)
        if m is not None:# No bag
            bagTable[m.group(1)] = []
        elif g == "":
            pass
        else:
            print 
            assert False


def bagContainsShine(bag, depth, number):
    count = 0
    # print(f" ##{bag}##")
    bag = bag.strip()
    if not bag in bagTable:
        bag = bag[:-1]
    assert (bag in bagTable), f"'{bag}' not found"
    if len(bagTable[bag]) == 0:
        print("   "*depth + f"{bag} * {number} of empty")
        return number
    for bb in bagTable[bag]:
        # print("   "*depth + bb[0])
        #if bag == 'shiny gold bag':
        cc = bagContainsShine(bb[0], depth+1, bb[1])
        print("   "*depth + f"{bb[0]}:{cc}" )
        #    count = 0
        count += cc
        #found = found or bagContainsShine(bb[0], depth +1)
    ttoal = (count+1) * number
    print("   "*depth + f"Total {bag} contains {ttoal}")
    return ttoal

# print (bagTable)
# print (bagTable)
bag = 'shiny gold bag'
count = bagContainsShine(bag, 0, 1) -1

print(count)
