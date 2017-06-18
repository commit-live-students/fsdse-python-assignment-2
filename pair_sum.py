def pairSum(l,n):
    if len(l) >= 2:
        l1 = []
        for i in l:
            for j in l:
                if i+j == n:
                    l1.append((i,j))
                else:
                    pass
        return l1
