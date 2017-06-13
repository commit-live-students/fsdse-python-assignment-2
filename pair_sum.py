l = [1,2,3,4,5]
num = 5

def pairSum(l, num):
    new_l = []
    for num1 in l:
        all = [num2 for num2 in l if((num1 + num2) == num)]
        for num2 in all:
            new_l.append([num1,num2])
    return new_l

if len(l) > 2:
    output = pairSum(l,num)
    print output
