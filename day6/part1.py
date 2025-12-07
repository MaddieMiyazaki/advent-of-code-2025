import math 

with open ('input.txt', 'r') as f:
    lines = f.readlines()
    total=0
    n=len(lines[0].split())
    for i in range(n):              # loop through each column
        current=[]                  # store values in ith column
        for line in lines:          # and then each row
            current+=[line.split()[i]]
        if current[-1]=='*':
            total+=math.prod([int(i)for i in current[:-1]])
        else:
            total+=sum([int(i)for i in current[:-1]])
    print(total)