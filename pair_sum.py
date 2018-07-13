def pairSum(x,y):
    #Sum = 0
    outputlist = []

    if(len(x) > 2):
        for i in range(0,len(x)-1):
            for j in range(i+1,len(x)-1):
                if x[i] + x[j] == y:
                    outputlist.append((x[i], x[j]))
    return outputlist
