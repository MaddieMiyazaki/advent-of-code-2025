with open('input.txt') as g:
    count=0
    idxs=g.readlines()
    found_blank=False
    for idx in idxs:
        if found_blank:
            with open('input.txt') as f:
                ranges = f.readlines()
                for r in ranges:
                    if r.strip('\n')=='':
                        break
                    if int(r.strip().split('-')[0])<=int(idx.strip())<=int(r.strip().split('-')[1]):
                        count+=1
                        # print(f"{idx.strip()} is in range {r.strip()}")
                        break
                    
        if idx.strip()=='':
            found_blank=True
    print(count)
