import os
import re
import copy
print("day07")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)


pc =0
accumulator = 0
groups = [x.split("\n") for x in open(path).read().split("\n\n")]
program = []

def acc(value):
    global accumulator
    global pc
    pc += 1
    accumulator += value
    # print(f"acc {accumulator}")

def jmp(value):
    global pc
    pc += value
    # print(f"jmp {pc}")

def nop(value):
    global pc
    pc += 1
    # print(f"nop {value}")

code = {
    "acc": acc,
    "jmp": jmp,
    "nop": nop,
}

for group in groups:
    for g in group:
        print(f"content {g}")
        program.append(g.split(' '))

print (program)
orgPrgram = copy.deepcopy(program)
posToUpdate = 0
    
while(pc != len(program)):
    pc =0
    accumulator = 0
    program = copy.deepcopy(orgPrgram)
    knonwLocations = []
    while (program[posToUpdate][0] != "jmp"):
        posToUpdate += 1
    # print(f"chanegd {posToUpdate}")
    program[posToUpdate][0] = "nop"
    
    while(pc != len(program)):
        if pc in knonwLocations:
            break
        knonwLocations.append(pc)
        line = program[pc]
        code[line[0]](int(line[1]))
        # print(f"{posToUpdate} {pc} {line[0]} acc {accumulator}")
    posToUpdate += 1
print(pc)
print (accumulator)
