def merge(fresh,lower,higher):
    index_higher=len(fresh)
    index_lower=len(fresh)
    for i in range(len(fresh)):
        if fresh[i]>=lower:
            index_lower=i
            break
    for i in range(index_lower,len(fresh)):
        if fresh[i]>=higher:
            index_higher=i
            break

    if index_lower%2==0:
        if index_higher%2==0:
            fresh=fresh[:index_lower]+[lower,higher]+fresh[index_higher:]  
        else:
            fresh=fresh[:index_lower]+[lower]+fresh[index_higher:]
    else:
        if index_higher%2==0:
            fresh=fresh[:index_lower]+[higher]+fresh[index_higher:]
        else:
            fresh=fresh[:index_lower]+fresh[index_higher:]   
    #print(index_lower, index_higher)
    return fresh


# even indices are starts of ranges, odd indices are ends of ranges
# index_lower is where lower would be inserted (but a value greater than it current holds its place) - if index_lower is odd, lower is inside a range
# index_higher is where higher would be inserted (but a value greater than it current holds its place) - if index_higher is odd, higher is inside a range   

# print(merge([3,5,10,14,16,20],12,18))   #3,5 --> 3,5,10,20
# print(merge([3,5,10,14,16,20],12,15))   #3,4 --> 3,5,10,15,16,20
# print(merge([3,5,10,14,16,20],6,15))    #2,4 --> 3,5,6,15,16,20
# print(merge([3,5,10,14,16,20],6,18))    #2,5 --> 3,5,6,20
# print(merge([3,5,10,14,16,20],1,2))     #0,0 --> 1,2,3,5,10,14,16,20
# print(merge([3,5,10,14,16,20],22,24))   #6,6 --> 3,5,10,14,16,20,22,24



with open('myinput.txt') as f:
    fresh=[]
    count=0
    lines=f.readlines()
    for line in lines:
        if line.strip()=='':
            break
        fresh=merge(fresh,int(line.strip().split('-')[0]),int(line.strip().split('-')[1]))
    print(fresh)
    for i in range(len(fresh)//2):
        count+=fresh[2*i+1]-fresh[2*i]+1
    print(count)