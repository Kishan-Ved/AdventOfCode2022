# See the OUTPUT PRESENT BEFORE ALL ERRORS
x = 1
c = 0
s = 0
l = [20,60,100,140,180,220]
while c<220: # 220 is a random number that exceeds the input Inputs exceed 220, thus, scroll up and see the output number present before all errors
    
    inp = input()
    if inp=="noop": # Inputs exceed 220, thus, scroll up and see the output number present before all errors
        c+=1
        if c in l:
            s += c*x
    else:
        a,b = inp.split()
        b = int(b)
        if (c+1) in l:
            s += (c+1)*x
        elif (c+2) in l:
            s += (c+2)*x
        c+=2
        x+=b
    
print(s)
    
# Inputs exceed 220, thus, scroll up and see the output number present before all errors