mat = []
for i in range(700):
    temp = []
    for j in range(700):
        temp.append(".")
    mat.append(temp)
# print(mat)
max = 0

while True:
    s = input()
    if s=="q": # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    l1 = []
    l2 = s.split(" -> ")
    for item in l2:
        l1.append(list(map(int,(item.split(",")))))
    # print(l1)

    for i in range(len(l1)):
        if l1[i][1]>max:
            max = l1[i][1]

    for i in range(len(l1)-1):
        # print("A")
        if(l1[i][0]==l1[i+1][0]):  # Same column
            # print("c")
            if l1[i][1]<l1[i+1][1]:
                for j in range(l1[i][1],l1[i+1][1]+1):
                    mat[j][l1[i][0]] = "#"
            elif l1[i+1][1]<l1[i][1]:
                for j in range(l1[i+1][1],l1[i][1]+1):
                    mat[j][l1[i][0]] = "#"

        elif(l1[i][1]==l1[i+1][1]):  # Same row
            # print("B")
            if l1[i][0]<l1[i+1][0]:
                for j in range(l1[i][0],l1[i+1][0]+1):
                    mat[l1[i][1]][j] = "#"
            elif l1[i+1][0]<l1[i][0]:
                for j in range(l1[i+1][0],l1[i][0]+1):
                    mat[l1[i][1]][j] = "#"
        

for i in range(700):
    mat[max+2][i] = "#"

c=0
while True:
    # print("B")
    x=500
    y=0
    b = True
    while True:
        # print(x,y)
        if  x<1 or x>698:
            b = False
            break
        if mat[y+1][x] == ".":
            y+=1
        elif mat[y+1][x-1] == ".":
            x-=1
            y+=1
        elif mat[y+1][x+1] == ".":
            x+=1
            y+=1
        elif mat[y+1][x] != "." and mat[y+1][x-1] != "." and mat[y+1][x+1] != ".":
            mat[y][x] = "o"
            c+=1
            break     
    if x == 500 and y==0:
        break
print(c)