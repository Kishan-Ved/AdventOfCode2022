s = input()

for i in range(0,len(s)-4):
    f = True
    l = [s[i],s[i+1],s[i+2],s[i+3]]
    l.sort()

    for j in range(0,3):
        if(l[j]==l[j+1]):
            f = False
            break
    
    if(f == True):
        print(i+4)
        break
    l=[]


