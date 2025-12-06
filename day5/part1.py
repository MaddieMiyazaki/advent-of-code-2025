with open('input.txt') as g:
    count=0
    idxs=g.readlines()
    found_blank=False           # use to track when ranges stop and ids start
    for idx in idxs:            # loop through all ids (after the ranges)
        if found_blank:
            with open('input.txt') as f:
                ranges = f.readlines()
                for r in ranges:                    # loop through all ranges
                    if r.strip('\n')=='':           # stop once ranges stop
                        break
                    if int(r.strip().split('-')[0])<=int(idx.strip())<=int(r.strip().split('-')[1]):
                        count+=1                    # increment count if id is in range
                        # print(f"{idx.strip()} is in range {r.strip()}")
                        break                       # once id appears in one range no need to check other ranges       
        if idx.strip()=='':
            found_blank=True
    print(count)
