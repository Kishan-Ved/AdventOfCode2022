sum = 0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    inp=input()
    if(inp=="q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
     break
    l = len(inp)
    p1 = inp[0:int(l/2)]
    p2 = inp[int(l/2):l]
    for i in range(0,int(l/2)):
        if p1.find(p2[i])!=-1:
          ind = letters.index(p2[i])
          sum+=ind + 1
          break
                        
print(sum)