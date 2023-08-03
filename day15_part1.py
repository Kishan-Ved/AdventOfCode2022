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
# print(l)
# print(time.time())
st = set()
for i in range(0,len(l),2):
    s = set()
    l1 = l[i]
    l2 = l[i+1]
    # print(l1[0])
    d = abs(l1[0]-l2[0]) + abs(l1[1]-l2[1])
    d1 = abs(l1[1]-2000000)
    i = 0
    while d1<=d:
        s.add(l1[0]+i)  
        s.add(l1[0]-i) 
        d1+=1
        i+=1
    if l2[1] in s:
        s.remove(l2[1])
    st = st.union(s)
# print(time.time())
print(len(st))
# print(st)
