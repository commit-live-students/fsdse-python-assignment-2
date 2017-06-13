def pairSum(x,y):
    OutputList=[]

    if(len(x)>2):
        for i in range(0,len(x)-1):
            for j in range(i+1,len(x)):
                if x[i] + x[j] == y:
                    OutputList.append((x[i],x[j]))
    return OutputList
print pairSum([0,1,5,2,3,4], 5)
