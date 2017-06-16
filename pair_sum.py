def pairSum(l,n):
    result = []
    if len(l)<2:
        print('error')
    else:
        for i in  l:
            for j in l:
                if(i+j == n and not(i==j)):
                    result.append(tuple(sorted((i,j))))
    return list(set(result))
