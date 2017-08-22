def pairSum(l,n):
    b =[]
    length = len(l)
    for i in l:
        for j in l:
            if i + j == n and i <= j :
                c = (i,j)
                b.append(c)
    return b

'''
l = [1,2,3,4,5,6]
a = pairSum(l,6)
print a
'''
