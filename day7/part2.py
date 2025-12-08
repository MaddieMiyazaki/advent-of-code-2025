with open('input.txt') as f:
    lines = f.readlines()
    n=len(lines[0].strip())             # width
    current=[0]*n  # {index:routes} beams in current line

    for line in lines:
        new=[0]*n                         # {index:routes} beams in next line

        for i in range(n):
            if line.strip()[i]=='S':    # initial beam
                new[i]=1
            if line.strip()[i]=='^':    # split
                if current[i]!=0:        # if there's a beam above the splitter
                    new[i-1]+=current[i]
                    new[i+1]+=current[i]
            else:                       # pass through without splitting
                if current[i]!=0:
                    new[i]+=current[i]
        current=new

    print(sum(current))

# like pascals
# use dictionaries!! {index:route_count} #set 1 on both sides