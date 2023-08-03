s = input()
l = []

for i in range(0,len(s)-4):
    f = True
    for j in range(0,14):
        l.append(s[i+j])

    l.sort()

    for j in range(0,13):
        if(l[j]==l[j+1]):
            f = False
            break
    
    if(f == True):
        print(i+14)
        break
    l=[]


