def pairSum(list_1, no):
    pairSum_list = []
    for i in range(0, len(list_1)):
        for j in range(i+1, len(list_1)):
            if (list_1[i] + list_1[j] == no):
                c = (list_1[i], list_1[j])
                pairSum_list.append(c)
    return pairSum_list
