# Code takes nearly 66 seconds to execute

# filer = open("kishan2.py").read()
# filer = filer.replace("Sensor at x=","[")
# filer = filer.replace(": closest beacon is at x=","],[")
# filer = filer.replace(" y=","")
# filer = filer.replace("\n","],")
# filew = open("kishan2.py","w")
# filew.write(filer)

import kishan2
import time
l = kishan2.lst

# Code takes 66 seconds to execute

def check_dist(s):
    for item in s:
        c=0
        for i in range(0,len(l),2):
            md = abs(l[i][0]-item[0]) + abs(l[i][1]-item[1])
            sd = abs(l[i][0]-l[i+1][0]) + abs(l[i][1]-l[i+1][1])
            if md > sd:
                c+=1
        if c==25:
            if 0<=item[0]<=4000000 and 0<=item[1]<=4000000:
                # print(item)
                print(item[0]*4000000+item[1])
                return True
    return False

t1 = time.time()
st = set()
for i in range(0,len(l),2): # Iterates over sensors
    temp = set() # Coordinates of every point outside the diamond of that sensor
    # print((i/2)+1)
    l1 = l[i] # Sensor coordinates
    l2 = l[i+1] # Beacon coordinates
    d = abs(l1[0]-l2[0]) + abs(l1[1]-l2[1])
    for i in range(0,d+1):
        temp.add((l1[0]+d-i+1,l1[1]+i))
        temp.add((l1[0]-d+i-1,l1[1]+i))
        temp.add((l1[0]+d-i+1,l1[1]-i))
        temp.add((l1[0]-d+i-1,l1[1]-i))
    temp.add((l1[0],d+1))
    temp.add((l1[0],-(d+1)))
    # print(len(temp))
    b = check_dist(temp)
    if b==True:
        break
t2 = time.time()
# print(t2-t1)