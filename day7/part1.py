with open('input.txt') as f:
    lines = f.readlines()
    current=set()  # indices of beams in current line
    splits=0

    n=len(lines[0].strip())             # width

    for line in lines:
        new=set()                       # indices of beams in next line
        for i in range(n):
            if line.strip()[i]=='S':    # initial beam
                new.add(i)
            if line.strip()[i]=='^':    # split
                if i in current:        # if there's a beam above the splitter
                    splits+=1
                    new.add(i-1)
                    new.add(i+1)
            else:                       # pass through without splitting
                if i in current:
                    new.add(i)
        current=new

    print(splits)
