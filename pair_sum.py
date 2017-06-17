def pairSum(list1, n):
    if len(list1) < 2:
        return None
    list1.sort()
    resultlist = []
    for i in list1:
        for j in list1[list1.index(i)+1:]:
            if (i + j == n):
                resultlist.append((i, j))

    return resultlist
