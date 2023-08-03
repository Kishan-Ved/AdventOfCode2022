d = {}
i=0
while True:
    s = input()
    if(s == "q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    l = len(s)
    d.update({i:s})
    i+=1

max_score = 1

for i in range(1,l-1):
    for j in range(1,l-1):
        score = 1
        t = d[i][j]

        c=0
        for k in range(i-1,-1,-1):
            c+=1
            if(d[k][j]>=t):
                break
        score *= c

        c=0
        for k in range(i+1,l):
            c+=1
            if(d[k][j]>=t):
                break
        score *= c

        c=0
        for k in range(j-1,-1,-1):
            c+=1
            if(d[i][k]>=t):
                break
        score *= c

        c=0
        for k in range(j+1,l):
            c+=1
            if(d[i][k]>=t):
                break  
        score *= c

        if(score > max_score):
            max_score = score

print(max_score)
