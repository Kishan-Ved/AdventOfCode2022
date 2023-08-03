points = 0
while True:
    inp = input()
    if(inp == "q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    else:
        p,q = inp.split()
        if p=="A":
            if q=="X":
                points+=(3+0)
            elif q=="Y":
                points+=(1+3)
            else:
                points+=(2+6)
        elif p=="B":
            if q=="X":
                points+=(1+0)
            elif q=="Y":
                points+=(2+3)
            else:
                points+=(3+6)
        else:
            if q=="X":
                points+=(2+0)
            elif q=="Y":
                points+=(3+3)
            else:
                points+=(1+6)
print(points)
        