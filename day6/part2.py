import math 

with open ('input.txt', 'r') as f:
    lines = f.readlines()
    total=0
    n=len(lines[0].strip('\n')) # length of each line including spaces
    current=[]
    for i in range(n):          # loop through each column
        vertical_number=''

        for line in lines:
            vertical_number+=line[i]


        if vertical_number!=' '*len(lines):             # if vertical_number stilll stores a number (haven't reached gap)
            current+=[vertical_number]
        if vertical_number==' '*len(lines) or i==n-1:   # if gap reached or rightmost column reached
            # print(current)                            # eg ['3847+', '4146 ', '68   ']
            if current[0][-1]=='*':
                current[0]=current[0][:-1]
                total+=math.prod([int(i.strip()) for i in current])
            else:
                current[0]=current[0][:-1]
                total+=sum([int(i.strip())for i in current])
            current=[]                                  # once a column is completed and operation performed, reset current list 
    print(total)

                
# read the text file from left to right, top to bottom
# store the current list of vertical numbers of a single column as a list, then perform the operation andd add to total
# reset current list after operation     
# continue until rightmost column is reached  

