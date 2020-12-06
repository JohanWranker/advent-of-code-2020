import os
import re
print("day06")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)



with open(path) as file:
    text = []
    gg = []
    count = 0

    new_group = False
    for line in file:
        #print(line)
        if line.strip() == "":
            #print("new")
            gg.append([count, text])
            text = []
            count = 0
        else:
            count += 1
            text += line.strip()

    gg.append([count, text])
    sum = 0
    for h in gg:
        print (h)
        for v in set(h[1]):
            co = h[1].count(v)
            if co == h[0]:
                sum += 1
            print (f"{v}:  {co} ")
        print (f"{h[1]}")

#        if allTrue:
#            sum += len(set(h[1]))

        print("###########")

    print (sum)