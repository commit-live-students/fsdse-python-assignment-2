def pairSum(l,n):
    sum = []
    for i in range(0,len(l)):
        for j in range(0,len(l)-1):
            if(l[i]+l[j]==n):
                sum.append((l[i],l[j]))
    return sum

tst = pairSum([1,2,3,4],5)
print tst
