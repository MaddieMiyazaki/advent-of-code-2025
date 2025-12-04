def find_largest(bank: str):
    idx_max=-1 # index of digit that was last selected
    joltage=''
    for i in range(12):
        m=max(list(bank[idx_max+1:len(bank)-11+i])) # see below
        idx_max=list(bank).index(m,idx_max+1)
        joltage+=str(m)
    return int(joltage)

# bank of length n 
# 0  :n-11 --> i
# i+1:n-10 --> j
# j+1:n-9  --> k
# ...
# y+1:n    --> z

with open("input.txt","r") as f:
    total=0
    for line in f.readlines():
        total+=find_largest(line.strip())
    print(total)    

