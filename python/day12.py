import os
import re
from datetime import datetime
import time
import copy

print("day12")
path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)
rawtext = open(path).readlines()

ship_pos = [0, 0]
waypoint_rel_pos = [10, 1]

Right = [ [0,1],[-1,0]]
Left =  [ [0,-1],[1,0]]

directions = { 
    'N' : [0,1],
    'E' : [1,0],
    'S' : [0,-1],
    'W' : [-1,0],
} 

for line in rawtext:
    order = line[:1]
    value = int(line[1:])
    if order in directions:
        waypoint_rel_pos[0] += value*directions[order][0]
        waypoint_rel_pos[1] += value*directions[order][1]
    if order == 'F':
        ship_pos[0] += waypoint_rel_pos[0]*value
        ship_pos[1] += waypoint_rel_pos[1]*value
    if order =='R':
        for i in range(int(value/90)):
            waypoint_rel_pos = [ 
                waypoint_rel_pos[0] * Right[0][0] + waypoint_rel_pos[1] * Right[0][1], 
                waypoint_rel_pos[0] * Right[1][0] + waypoint_rel_pos[1] * Right[1][1], 
                ]
    if order =='L':
        for i in range(int(value/90)):
            waypoint_rel_pos = [ 
                waypoint_rel_pos[0] * Left[0][0] + waypoint_rel_pos[1] * Left[0][1], 
                waypoint_rel_pos[0] * Left[1][0] + waypoint_rel_pos[1] * Left[1][1], 
                ]
    # print (f"'{order}'{value}'  {ship_pos} {dirction} [ {waypoint_rel_pos}]")
print(f"{abs(ship_pos[0])+ abs(ship_pos[1])}")
assert 29839 == abs(ship_pos[0])+ abs(ship_pos[1])


