max = 0
sum = 0
while True:
    inp = input() # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
    if(inp == "q"):
        break
    elif(inp == ""):
        if sum>max:
            max = sum
        sum = 0
    else:
        sum += int(inp)    

print(max)