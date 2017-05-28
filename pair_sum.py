def pairSum(x,y):
    Sum = 0
    outputlist = []

    if(len(x) > 2):
        for i in range(0,len(x)-1):
            Sum = x[i]+x[i+1]
            if Sum == y:
                outputlist.append((x[i], x[i+1]))

        return outputlist
    print outputlist
