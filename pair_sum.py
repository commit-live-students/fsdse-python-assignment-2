
def pairSum(numList, num):
    if len(numList) < 2:
        print('Enter atleast 2 integers in the list')
        return 1
    for i in numList:
        if type(i) != int:
            print('Enter integers in the list')
            return 2

    newLst = []
    for n1 in numList:
        lst = [n2 for n2 in numList if((n1 + n2) == num)]
        for item in lst:
            newLst.append([n1,item])
    return newLst
print(pairSum([5,6,1,10,4,7],10))
