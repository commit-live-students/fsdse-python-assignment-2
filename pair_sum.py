def pairSum(aList, thesum):
    aList.sort()
    pairs = []
    a = 0
    b = len(aList) - 1
    while a < b:
        pairsum = aList[a] + aList[b]
        if pairsum == thesum:
            pairs.append((aList[a], aList[b]))
            a += 1
        else:
            b -=1

    return pairs
