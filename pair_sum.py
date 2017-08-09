def pairSum(list, number):
    output = []
    if len(list) >= 2:
        for i in list:
            for j in list:
                if i + j == number and (j,i) not in output:
                    output.append((i,j))
    return output


print pairSum([1,2,3,4],5)
