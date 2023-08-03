c=0
while True:
    inp = input()
    if(inp=="q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    p1,p2 =  inp.split(",")
    l1,u1 = p1.split("-")
    l2,u2 = p2.split("-")
    l1 = int(l1)
    l2 = int(l2)
    u1 = int(u1)
    u2 = int(u2)
    if (l2<=u1 and l1<=l2) or (l1<=u2 and l2<=l1):
        c+=1

print(c)
