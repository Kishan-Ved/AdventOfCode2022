import math
d = {0:[97, 81, 57, 57, 91, 61],1:[88, 62, 68, 90],2:[74, 87],3:[53, 81, 60, 87, 90, 99, 75],4:[57],5:[54, 84, 91, 55, 59, 72, 75, 70],6:[95, 79, 79, 68, 78],7:[61, 97, 67]}
l = [0,0,0,0,0,0,0,0]
for i in range(20):
    d[0] = list(map(lambda x: math.floor((x*7)/3),d[0]))
    for item in d[0]:
        if item%11==0:
            d[5].append(item)
        else:
            d[6].append(item)
        
        l[0]+=1
    d[0] = []
    # print(d)
    # print(l)
    d[1] = list(map(lambda x: math.floor((x*17)/3),d[1]))
    for item in d[1]:
        if item%19==0:
            d[4].append(item)
        else:
            d[2].append(item)
        
        l[1]+=1
    d[1] = []
    # print(d)
    # print(l)
    d[2] = list(map(lambda x: math.floor((x+2)/3),d[2]))
    for item in d[2]:
        if item%5==0:
            d[7].append(item)
        else:
            d[4].append(item)
        
        l[2]+=1
    d[2] = []
    # print(d)
    # print(l)
    d[3] = list(map(lambda x: math.floor((x+1)/3),d[3]))
    for item in d[3]:
        if item%2==0:
            d[2].append(item)
        else:
            d[1].append(item)
        
        l[3]+=1
    d[3] = []
    # print(d)
    # print(l)
    d[4] = list(map(lambda x: math.floor((x+6)/3),d[4]))
    for item in d[4]:
        if item%13==0:
            d[7].append(item)
        else:
            d[0].append(item)
        
        l[4]+=1
    d[4] = []
    # print(d)
    # print(l)
    d[5] = list(map(lambda x: math.floor((x*x)/3),d[5]))
    for item in d[5]:
        if item%7==0:
            d[6].append(item)
        else:
            d[3].append(item)
        
        l[5]+=1
    d[5] = []
    # print(d)
    # print(l)
    d[6] = list(map(lambda x: math.floor((x+3)/3),d[6]))
    for item in d[6]:
        if item%3==0:
            d[1].append(item)
        else:
            d[3].append(item)
        
        l[6]+=1
    d[6] = []
    # print(d)
    # print(l)
    d[7] = list(map(lambda x: math.floor((x+4)/3),d[7]))
    for item in d[7]:
        if item%17==0:
            d[0].append(item)
        else:
            d[5].append(item)
        
        l[7]+=1
    d[7] = []
    # print(i)
    
    # print(d)
    # print(l)

# print(l)
l.sort()
# print(l)
print(l[-1]*l[-2])
