import math

with open('input.txt','r') as f:            
    lines=f.readlines()
    n=len(lines)        # number of boxes
    min_dist={}         # {(0,1):200,(0,2):300 ...}

    # find all shortest distances
    for box1 in range(n):
        for box2 in range(n):
            if box1<box2:
                coords1=[int(i) for i in lines[box1].split(',')]
                coords2=[int(i) for i in lines[box2].split(',')]
                dist=(coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2+(coords1[2]-coords2[2])**2
                min_dist[(box1,box2)]=dist     

    min_dist={k:v for k,v in sorted(min_dist.items(), key=lambda x:x[1])}

    # define circuits
    # neither in a circuit (0,0): create new circiut
    # on in a circuit the other not (0,2): join to circuit
    # in two different circuits (1,2): join two circuits
    # in same circuit (1,1): no action

    circuits=[0]*n              # eg [1, 0, 2, 0, 0, 0, 0, 1, 2, 4, 0, 5, 4, 2, 1, 0, 5, 2, 2, 1] for 20 boxes input
    circuit_no=1

    for pair in list(min_dist.keys()):
        c0=circuits[pair[0]]
        c1=circuits[pair[1]]

        if (c0,c1) == (0,0):       # neither in a circuit
            circuits[pair[0]]=circuit_no
            circuits[pair[1]]=circuit_no
            circuit_no+=1
        else:
            if c0*c1==0:           # only one already exists in a circuit: join to existing circuit
                c=c0+c1
                circuits[pair[0]]=c
                circuits[pair[1]]=c
            elif c0!=c1:           # both belong to two different circuits merge two circuits
                c=min(c0,c1)        # taking min ensures all circuits end up in 'circuit 1' eventually
                for i in range(n):
                    if circuits[i]==c1 or circuits[i]==c0:
                        circuits[i]=c
            else :                 # no action since two pair are already in same circuit
                pass 
       
        # print(pair,circuits)
        if circuits==[1]*n:             # stop once all boxes are in 'circuit 1'
            print(int(lines[pair[0]].split(',')[0])*int(lines[pair[1]].split(',')[0]))
            break
