def near(hx,hy,tx,ty):
    if(abs(hx-tx)==1 and hy==ty):
        return True
    if(abs(hy-ty)==1 and hx==tx):
        return True
    if(abs(hx-tx)==1 and abs(hy-ty)==1):
        return True
    if(hx==tx and hy==ty):
        return True
    return False
    
l = []
h=[0,0]
t=[0,0]
tset = {(0,0)}
while True:
    s = input()
    if s=="q": # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    d,n = s.split()
    n = int(n)
    for i in range(n):
        hi=h.copy()
        if d == "R":
            h[0]+=1
        elif d == "L":
            h[0]-=1
        elif d=="U":
            h[1]+=1
        elif d=="D":
            h[1]-=1
        
        if near(h[0],h[1],t[0],t[1]):
            continue
        else:
            t[0] = hi[0]
            t[1] = hi[1]
            tup = tuple(t)
            tset.add(tup)
# print(tset)
print(len(tset))



    
