def adj(rolls): #input matrix (list of strings)
    rolls=[list(row) for row in rolls]   # convert to list of lists for mutability
    total=0
    removed=-1      # initalise at non-zero to enter loop
    
    # iterate till no more can be removed
    while removed!=0:
        removed=0
        for i in range(len(rolls)):
            for j in range(len(rolls[i])):
                if rolls[i][j]=='@':
                    adjacent=0
                    surrounding=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                    for cell in surrounding:
                        if 0<=cell[0]<=len(rolls)-1 and 0<=cell[1]<=len(rolls[i])-1:        # only check if index exists
                            if rolls[cell[0]][cell[1]]=='@':
                                adjacent+=1
                    if adjacent<4:
                        total+=1
                        removed+=1
                        rolls[i][j]='.'        # 'remove' roll (possible since rolls is list of lists)
    return total


with open('input.txt','r') as f:
    data=f.read().splitlines()
    print(adj(data))


# unlike the example given in AoC where all 'valid' rolls are removed simultaneously,
# this code removes the roll as soon as a 'valid' roll is found