with open('input.txt') as f:
    lines = f.readlines()
    n=len(lines[0].strip())             # width
    current=[0]*n                       # routes to ith index  in current line

    for line in lines:
        new=[0]*n                       # routes to ith index in next line
        for i in range(n):
            if line.strip()[i]=='S':    # initial beam
                new[i]=1                # only one timeline
            if line.strip()[i]=='^':    # split
                new[i-1]+=current[i]
                new[i+1]+=current[i]
            else:                       # pass through without splitting
                new[i]+=current[i]
        current=new                     # eg [0, 0, 1, 0, 5, 0, 4, 3, 4, 0, 2, 0, 1, 0, 0]
        # print(current)
    print(sum(current))

# pascals-triangle-esque approach: 
# work through each line and log number of possible routes to ith index in list 'current'
# at next line count routes to ith index by summing from any legal routes in line above, then update current