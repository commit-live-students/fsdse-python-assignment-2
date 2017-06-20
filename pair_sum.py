def pairSum(x,sum):
    List = []
    s = set(x)

    for i in x:
        diff = sum-i
        s.remove(i)
        if diff in s:
            t = (i, diff)
            List.append(t)
    return List
                    


L = [1,2,3,4]
sum = 5
pairSum(L,sum)
