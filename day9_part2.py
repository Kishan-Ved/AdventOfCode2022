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
    
l = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
tset = {(0,0)}
while True:
    s = input()
    if s=="q": # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    d,n = s.split()
    n = int(n)
    
    for j in range(n):

        if d == "R":
            l[0][0]+=1
        elif d == "L":
            l[0][0]-=1
        elif d=="U":
            l[0][1]+=1
        elif d=="D":
            l[0][1]-=1
            
        for i in range(9):
            if near(l[i][0],l[i][1],l[i+1][0],l[i+1][1]):
                break
            else:
                if(l[i][0]>l[i+1][0] and l[i][1]==l[i+1][1]):
                    l[i+1][0]+=1
                if(l[i][0]<l[i+1][0] and l[i][1]==l[i+1][1]):
                    l[i+1][0]-=1
                if(l[i][1]>l[i+1][1] and l[i][0]==l[i+1][0]):
                    l[i+1][1]+=1
                if(l[i][1]<l[i+1][1] and l[i][0]==l[i+1][0]):
                    l[i+1][1]-=1
                if(l[i][0]>l[i+1][0] and l[i][1]>l[i+1][1]):
                    l[i+1][0]+=1
                    l[i+1][1]+=1
                if(l[i][0]>l[i+1][0] and l[i][1]<l[i+1][1]):
                    l[i+1][0]+=1
                    l[i+1][1]-=1
                if(l[i][0]<l[i+1][0] and l[i][1]>l[i+1][1]):
                    l[i+1][0]-=1
                    l[i+1][1]+=1
                if(l[i][0]<l[i+1][0] and l[i][1]<l[i+1][1]):
                    l[i+1][0]-=1
                    l[i+1][1]-=1


        tup = tuple(l[9])   
        tset.add(tup)

# print(tset)
print(len(tset))



    
