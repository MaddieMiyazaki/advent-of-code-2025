with open('input.txt','r') as f:
    rows=f.readlines()
    total=50
    count=0
    for row in rows:
        if row[0]=='L':
            total=(total-int(row[1:]))%100
        else:
            total=(total+int(row[1:]))%100
        if total==0:
            count+=1
    print(count)