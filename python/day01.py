import os
print("day01")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

with open(path) as file:
    list = [int(line.strip()) for line in file]

list.sort()
for i in list:
    for j in list:
        if i+j == 2020:
            print(i*j)
            exit(0)
        if j>2020/2:
            break
print("OOOPS fail")



