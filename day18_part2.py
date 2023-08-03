# Code takes nearly 5 minutes to execute

l = []
while True:
    inp = input()
    if inp=="q": # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    l.append(tuple(map(int,inp.split(","))))
# print(len(l))

def f(x,y,z): # Checks if the cube forms outer surface 
    temp = [(x,y,z)]
    s = set()
    
    while temp: # Covers all elements in temp
        cube = temp[0]
        temp.remove(cube)
        x,y,z = cube
        if cube in l: # As if all are in l, we have to return False after exiting the loop
            continue
        if cube in s: # As it has been checked first and we do not need to check it again and it got added in s only if it was not in l
            continue
        s.add(cube)
        if x<0 or x>21 or y<0 or y>21 or z<0 or z>21: # As now, cubes go outside the range of input
            return True
        temp.append((x+1,y,z))
        temp.append((x-1,y,z))
        temp.append((x,y+1,z))
        temp.append((x,y-1,z))
        temp.append((x,y,z+1))
        temp.append((x,y,z-1))
    return False

# Code takes nearly 5 minutes to execute

c=0 # Counter variable to count number of free surfaces 
i=0
for cube in l:
    x,y,z = cube
    if f(x+1,y,z): 
        c+=1
    if f(x-1,y,z):
        c+=1
    if f(x,y+1,z):
        c+=1
    if f(x,y-1,z):
        c+=1
    if f(x,y,z+1):
        c+=1
    if f(x,y,z-1):
        c+=1 
    # print(i) 
    i+=1
    
print(c)

# Code takes nearly 5 minutes to execute