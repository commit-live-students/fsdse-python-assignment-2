def pairSum(l,n):
    obj=list()
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if i!=j:
                if n==l[i]+l[j]:
                    obj.append((l[i],l[j]))
    return obj
print(pairSum([2, 5, 4, 3, 8, 7, 6, 1, 10, -1], 9))
