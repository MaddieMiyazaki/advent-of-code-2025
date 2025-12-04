def not_valid_1(num):
    n=len(str(num))
    if n%2==0:
        if str(num)==str(num)[:n//2]*2:
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
            if not_valid_1(i):
                total+=i
    print(total)