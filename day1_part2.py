s = []
sum = 0
while True:
    inp = input() # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
    if(inp == "q"):
        break
    elif(inp == ""):
        s.append(sum)
        sum=0
    else:
        sum += int(inp)   

s.sort()
a = s[-1] + s[-2] + s[-3]
print(a)