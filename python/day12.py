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
dirction = 'E'

directions = ['N','E','S','W']

for line in rawtext:
    order = line[:1]
    value = int(line[1:])
    if order == 'N':
        waypoint_rel_pos[1] += value
    if order == 'S':
        waypoint_rel_pos[1] -= value
    if order == 'E':
        waypoint_rel_pos[0] += value
    if order == 'W':
        waypoint_rel_pos[0] -= value
    if order in ['F', 'B']:
        ship_pos[0] = ship_pos[0] + waypoint_rel_pos[0]*value
        ship_pos[1] = ship_pos[1] + waypoint_rel_pos[1]*value
    if order =='R':
        for i in range(int(value/90)):
            waypoint_rel_pos = [waypoint_rel_pos[1], -waypoint_rel_pos[0]]
    if order =='L':
        for i in range(int(value/90)):
            waypoint_rel_pos = [-waypoint_rel_pos[1], waypoint_rel_pos[0]]
    print (f"'{order}'{value}'  {ship_pos} {dirction} [ {waypoint_rel_pos}]")
print(f"{abs(ship_pos[0])+ abs(ship_pos[1])}")

