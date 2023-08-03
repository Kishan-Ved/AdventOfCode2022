l = []
while True:
    inp = input()
    if(inp=="q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    l.append(list(map(int,inp.split(","))))
# print(len(l))

# print(l)
sa = 0
for cube in l:
    x,y,z = cube
    c=0
    if [x+1,y,z] in l:
        c+=1
    if [x-1,y,z] in l:
        c+=1
    if [x,y+1,z] in l:
        c+=1
    if [x,y-1,z] in l:
        c+=1
    if [x,y,z+1] in l:
        c+=1
    if [x,y,z-1] in l:
        c+=1
    sa = sa + 6 - c
    # print(sa)
print(sa)

maxx = 10
minx = 0

for cube in l:
    if cube[0]>maxx:
        maxx = cube[0]
    if cube[0]<minx:
        minx = cube[0]
    

