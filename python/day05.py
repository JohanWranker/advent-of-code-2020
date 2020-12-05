import os
import re
print("day05")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

def codes(max, width):
    rowDict = {}
    for ro in range(0,max):
        r = ro + 0.5
        half = max/2
        code = ''
        for i in range(width):
            if r < half:
                code += 'F'
            else:
                r -= half
                code += 'B'
            half = half/2
        print(f"row {ro} {code}")
        rowDict[code] = ro
    return rowDict

def codesL(max, width):
    rowDict = {}
    for ro in range(max):
        r = ro + 0.5
        half = max/2
        code = ''
        print(f"seat {ro}")
        index = 0
        for i in range(width):
            code += 'L' if (r < half ) else 'R'
            r = r % half
            half = half/2
        rowDict[code] = ro
    return rowDict

#rowDict = codes(128, 6)
rowDict = codes(128, 7)
print (rowDict)


seatDict = codesL(8, 3)
print (seatDict)


data = 'BFFFBBFRRR'
row = rowDict[data[0:7]]
seat = seatDict[data[-3:]]
pos = row*8 + seat
print (f"row {row} {seat} {pos}")

maxpos = 0
occupedSeats = []
with open(path) as file:
    for line in file:
        print(line)
        pos = rowDict[line[0:7]]*8 + seatDict[line[7:10]]
        occupedSeats.append(pos)
        maxpos = pos if pos > maxpos else maxpos

for p in range(rowDict['BBBBBBB']*8 + seatDict['RRR']):
    if p not in occupedSeats:
        print(f"pos {p} not in list ")