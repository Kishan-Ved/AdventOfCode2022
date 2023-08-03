grid = []
r=0
while True:
    inp = input()
    if inp=="q": # Used to take input, copy and paste it in the console. Type q in the next line to start the execution of the program
        break
    temp  = []
    for char in inp:
        if char!="S" or char!="E":
            char = int(ord(char))
        temp.append(char)
    grid.append(temp)
    if "S" in inp:
        S = (r,inp.find("S"))
    if "E" in inp:
        E = (r,inp.find("E"))
    r+=1

xs,ys = S
grid[xs][ys] = 97

xe,ye = E
grid[xe][ye] = 122

n_rows = len(grid)
n_columns = len(temp)
# print(grid)
# print(S)
# print(E)
# print(n_columns)
# print(n_rows)

l = [S]
dict = {S:0}
s = set(S)
d = [(0,1),(0,-1),(1,0),(-1,0)]

while l:
    if l[0] == E:
        break
    x,y = l[0] # x - row and y - column
    l.pop(0)
    for dx,dy in d:
        if (x+dx,y+dy) in s:
            continue
        if x+dx >= n_rows or x+dx < 0 or y+dy >= n_columns or y+dy < 0:
            continue
        # print((x+dx,y+dy),(x,y))
        if grid[x+dx][y+dy] <= grid[x][y] + 1:
            l.append((x+dx,y+dy))
            s.add((x+dx,y+dy))
            dict.update({(x+dx,y+dy):(dict[(x,y)]+1)})
            if (x+dx,y+dy) == E:
                break

# print(dict[(1,1)])
print(dict[E])
