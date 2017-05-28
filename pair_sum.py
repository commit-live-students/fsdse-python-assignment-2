def pairSum(list,n):
    pairList = [];
    if len(list) < 2:
        return list
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if(list[i]+list[j] == n):
                pairList.append([list[i],list[j]])
    return pairList
