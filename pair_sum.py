def pairSum(inputList , num):

    pair = ()
    outList = []

    if(len(inputList) < 3):
        print "Size of list should be greater then 2"

    for i in range(0,len(inputList)):
        print i
        for j in range(i+1,len(inputList)):
            print j
            if (inputList[i] + inputList[j] == num):
                pair = (inputList[i] , inputList[j])
                outList.append(pair)
    return outList            

print pairSum([1,5,3,4,5,6] , 10)
