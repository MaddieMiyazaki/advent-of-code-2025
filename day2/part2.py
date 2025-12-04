def not_valid_2(num):
    n=len(str(num))
    # list factors including itself, excluding 1
    list_of_factors=[i for i in range(2,n+1) if n%i==0]
    for factor in list_of_factors:
        if str(num)==str(num)[:n//factor]*factor:
            return True
    return False

# return true if number is a sequence repeated twice

with open('input.txt','r') as f:
    data=f.read().split(',')
    total=0
    for r in data:
        low=int(r.split('-')[0])
        high=int(r.split('-')[1])
        for i in range(low,high+1):
            if not_valid_2(i):
                total+=i
    print(total)


# not_valid_2 function checks if the inout number is made up of a repeating sequence
# initially find list of factors including itself but not 1, 
# then check if the number cna be writeen as a repeating sequence with length n/factor