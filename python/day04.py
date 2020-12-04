import os
import re
print("day04")

path = "input"
if not os.path.exists(path):
    print(" File not exist ", os.path.abspath(path))
    exit(1)

count = 0
match = 0

def check_count():
    global count 
    global match 
    if (count == 7):
        match += 1
    count = 0
    print("end passport")

with open(path) as file:
    for line in file:
        print(line)
        m = re.findall(r'\s?((\S+):(\S+))', line)
        if len(m):
            for item in m:
                code = item[1]
                value = item[2]
                if code == 'cid':
                    print ("ignored")
                    continue;
                elif code == 'byr':
                    if int(value) >= 1920 and int(value) <= 2002:
                        print ("valid")
                        count += 1
                elif code == 'iyr':
                    if int(value) >= 2010 and int(value) <= 2020:
                        print ("valid")
                        count += 1
                elif code == 'eyr':
                    if int(value) >= 2020 and int(value) <= 2030:
                        print ("valid")
                        count += 1
                elif code == 'hgt':
                    mm = re.match(r'(\d+)(in|cm)',value)
                    if mm is None:
                        print ("invalid")
                        continue
                    type = mm[2]
                    length = int(mm[1])
                    if (type == 'cm'and length >= 150 and length <= 193) or \
                        (type == 'in'and length >= 59 and length <= 76):
                            print ("valid")
                            count += 1
                elif code == 'hcl':
                    if value[0] == "#" and value[1] in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                        print ("valid")
                        count += 1
                elif code == 'ecl':
                    if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
                        print ("valid")
                        count += 1
                elif code == 'pid' and re.match(r'^\d{9}$',value):
                        print ("valid")
                        count += 1
                else:
                    print ("invalid")
        else:
            check_count()
            count = 0


check_count()
print(f"mathces {match}")
