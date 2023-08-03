l = []
sum = 0

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
    
for item in l:
    if(item <= 100000):
        sum += item

print(sum)
# print(l)

# The input needs 2 lines of $ cd .. at the end as they are missing in the question  
    
    

        
                

        
