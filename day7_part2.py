#space available : 70000000 - 41609574 = 28390426
#extra space needed : 30000000 - 28390426 = 1609574

l = []

def size():
    s = 0
    while True:
        inp = input()
        if(inp == "$ cd .."):
            l.append(s)
            return s
        if(inp.startswith("$ cd ")):
            s = s + size()
        inp = inp.split()
        if(inp[0].isdigit()): 
            s = s + int(inp[0])
        
        else:
            continue

while True:
    s = input()
    if(s=="q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        # The input needs 2 lines of $ cd .. at the end as they are missing in the question  
        break
    elif(s.startswith("$ cd ")):
        size()

min = 100000000000
for item in l:
    if(item >= 1609574):
        if(min>item):
            min = item

print(min)

# The input needs 2 lines of $ cd .. at the end as they are missing in the question  
    
    

        
                

        
