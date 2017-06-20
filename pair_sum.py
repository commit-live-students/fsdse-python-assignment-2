def pairSum(l,n):
    a=[]
    if len(l)>2:
        for i in l:
            for j in l:
                if(i+j==n) and not(i==j):
                    a.append((i,j))
    return list(set(tuple(sorted(l)) for l in a))
