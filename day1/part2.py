with open('input.txt','r') as f:
    rows=f.readlines()
    total=50
    count=0
    extra=0
    for row in rows:

        if row[0]=='L': 
            if total==0:
                extra=-1
            total-=int(row[1:])       
        else:  
            total+=int(row[1:])
            
        if total<=0:
            count+=int((100-total)/100)+extra
        else:
            count+=int(total/100) +extra

        extra=0
        total=total%100

    print(count)

# count is incremented when total crosses multiples of 100
# 299 ~ 200 -> 2
# 199 ~ 100 -> 1
# 99  ~ 1   -> 0

# 0 ~ -99 -> 1
# -100 ~ -199 -> 2
# -200 ~ -299 -> 3


# extra functionality: if already at 0 and turn left (eg 0--> -5), need to decrement count by 1