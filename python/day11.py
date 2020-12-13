import os
import re
from datetime import datetime
import time
import copy

print("day11")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)
rawtext = open(path).readlines()

seats = [list(x.strip()) for x in rawtext]

directions = [ [1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1] ]

def isOccupied(rowId, seatId, direction):
    y = direction[0]+ rowId
    x = direction[1]+ seatId
    if x < 0 or x >= len(seats[0]) or \
        y < 0 or y >= len(seats):
        return False
    if seats[y][x] != '.':
        return seats[y][x] == 'X'
    return isOccupied(y,x,direction)

output = seats
updated = True
loop = 0
while (updated):
    loop +=1
    updated = False
    seats = copy.deepcopy(output)
    for rowId in range(len(seats)):
        for seatId in range(len(seats[0])):
            # Test if empty
            if seats[rowId][seatId] == 'L':
                for d in directions:
                    if isOccupied(rowId, seatId, d):
                        break
                else: 
                    output[rowId][seatId] = 'X'
                    updated = True
            # test if leave
            elif seats[rowId][seatId] == 'X':
                count = 0
                for d in directions:
                    count += 1 if isOccupied(rowId, seatId, d) else 0
                if count >= 5:
                    output[rowId][seatId] = 'L'
                    updated = True
    
    # for x in output:
    #    print(''.join(x))
    # print(f"{loop}")
count = sum(x.count('X') for x in output)

print(f"count {count}")
assert 2197 == count