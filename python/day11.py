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

data = ["."*4 +x.strip() + "."*4 for x in rawtext]
floor = ["."*len(data[0])]*4
emptySlot = ['LLL', '.LL', '.L.', 'LL.']
overCOccupied = ['XXXX']
output = floor + data + floor
while (True):
    seats = copy.deepcopy(output)
    transposed = [''.join(seats[j][i] for j in range(len(seats))) for i in range(len(seats[0]))] 
    output = []
    for rowId in range(len(seats)):
        out = list(seats[rowId])
        if rowId >= 4 and rowId <= len(seats)-4:
            for seatId in range(4, len(seats[0])-4):
                a = seats[rowId][seatId-1:seatId+2]
                if seats[rowId][seatId-1:seatId+2] in emptySlot:
                    b = transposed[seatId][rowId-1:rowId+2]
                    if transposed[seatId][rowId-1:rowId+2] in emptySlot:
                        out[seatId] = 'X'
                c = seats[rowId][seatId-3:seatId+1]
                d = seats[rowId][seatId:seatId+4]
                if seats[rowId][seatId-3:seatId+1] in overCOccupied or \
                    seats[rowId][seatId:seatId+4] in overCOccupied:
                    out[seatId] = 'L'
                if transposed[seatId][rowId-3:rowId+1] in overCOccupied or \
                    transposed[seatId][rowId:rowId+4] in overCOccupied:
                    out[seatId] = 'L'
        output.append(''.join(out))

    for x in output:
        print(x)
