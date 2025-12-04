def find_largest(bank):
    m=0     # initialise maximum digit
    idx_max=-1 # earliest index of the largest digit
    for i in range(len(str(bank))-1):
        if int(str(bank)[i])>m:
            idx_max=i
            m=int(str(bank)[i])
    
    unit=max([int(i) for i in list(str(bank)[idx_max+1:])]) # find largest digit from remaining
    return 10*int(str(bank)[idx_max])+unit


with open("input.txt","r") as f:
    total=0
    for line in f.readlines():
        total+=find_largest(line.strip())
    print(total)    

