d = {}
i=0
while True:
    s = input()
    if(s == "q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    l = len(s)
    d.update({i:s})
    i+=1
trees = 0

for i in range(1,l-1):
    for j in range(1,l-1):
        t = d[i][j]
        c=0
        for k in range(0,i):
            if(d[k][j]>=t):
                c+=1
                break
        for k in range(i+1,l):
            if(d[k][j]>=t):
                c+=1
                break
        for k in range(0,j):
            if(d[i][k]>=t):
                c+=1
                break
        for k in range(j+1,l):
            if(d[i][k]>=t):
                c+=1
                break            
        if(c==4):
            trees += 1

print(l*l-trees)
