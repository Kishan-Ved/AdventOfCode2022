# filer = open("kishan.py").read()
# filer = filer.replace("\n\n",",")
# filer = filer.replace("\n",",")
# filew = open("kishan.py","w")
# filew.write(filer)

import kishan
l = kishan.lst
def decide(l1,l2):
    if type(l1)==int and type(l2)==int:
        if l1<l2:
            return 1
        if l1==l2:
            return 0
        return -1

    if type(l1)==int and type(l2)==list:
        l1 = [l1]

    if type(l1)==list and type(l2)==int:
        l2 = [l2]

    if type(l1)==list and type(l2)==list:
        m = min(len(l1),len(l2))
        for i in range(m):
            x = decide(l1[i],l2[i])
            if x==-1:
                return -1
            if x==1:
                return 1

        if len(l1)<len(l2):
            return 1
        if len(l1)==len(l2):
            return 0
        return -1

c = 0

for i in range(0,len(l),2):
    l1 = l[i]
    l2 = l[i+1]
    x = decide(l1,l2)
    if x==1:
        c+=i/2+1

print(c)