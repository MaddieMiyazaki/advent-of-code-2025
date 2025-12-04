def adj(rolls): #input matrix (list of strings)
    total=0
    for i in range(len(rolls)):
        for j in range(len(rolls[i])):
            if rolls[i][j]=='@':
                #print('current: ',i,j)
                adjacent=0
                surrounding=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                for cell in surrounding:
                    if 0<=cell[0]<=len(rolls)-1 and 0<=cell[1]<=len(rolls[i])-1:        # only check if index exists
                        if rolls[cell[0]][cell[1]]=='@':
                            adjacent+=1
                if adjacent<4:
                    total+=1
                #print('adjacent total:',adjacent)
    return total


with open('input.txt','r') as f:
    data=f.read().splitlines()
    print(adj(data))
