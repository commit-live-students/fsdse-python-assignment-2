def pairSum(_list,n):
    if len(_list)<2:
        return

    integer_pairs=[]
    pair_sum=0
    for i in range(len(_list)):
        for j in range(i+1, len(_list)):
            pair_sum = _list[i] + _list[j]
            if pair_sum==n:
                integer_pairs.append([_list[i], _list[j]])
    return integer_pairs
