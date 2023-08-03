d = {1:["B","S","J","Z","V","D","G"],2:["P","V","G","M","S","Z"],3:["F","Q","T","W","S","B","L","C"],
4:["Q","V","R","M","W","G","J","H"],5:["D","M","F","N","S","L","C"],6:["D","C","G","R"],
7:["Q","S","D","J","R","T","G","H"],8:["V","F","P"],9:["J","T","S","R","D"]}

# d = {1:["N","Z"],2:["D","C","M"],3:["P"]} Test Case

while True:
    inp = input()
    if(inp == "q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    inp = inp.split()
    n = int(inp[1])
    f = int(inp[3])
    l = int(inp[5])

    for i in range (0,n):
        d[l].insert(0,d[f][0])
        d[f].pop(0)

for i in range(1,10):
    print(d[i][0],end="")  