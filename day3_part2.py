sum=0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
    inp1 = input()
    if(inp1=="q"): # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
     break
    inp2 = input()
    inp3 = input()
    l3 = len(inp3)
    for i in range(0,l3):
        if inp1.find(inp3[i])!=-1 and inp2.find(inp3[i])!=-1:
          sum+=letters.index(inp3[i])+1
          break

print(sum)