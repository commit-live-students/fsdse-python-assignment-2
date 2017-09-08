def pairSum (lst, sum):
    pairs = []
    if len(lst) < 2:
        return []
    for i,num in enumerate(lst):
        for j in range (i+1,len(lst)):
            if num + lst[j] == sum:
                pairs.append(tuple((num, lst[j])))
    return pairs

if __name__ == "__main__":
    print pairSum ([3,5,5,7,9,11],10)
    #print pairsum (0)
    #print pairsum (100)
    #print pairsum (101)
