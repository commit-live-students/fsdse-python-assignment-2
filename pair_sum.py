def pairSum(l,n):
    a=[]
    if len(l)<2:
        print "The length of List is less than two"
    else:
        for i in l:
            for j in l:
                if(i+j==n) and not(i==j):
                    a.append((i,j))
    return list(set(tuple(sorted(l)) for l in a))
