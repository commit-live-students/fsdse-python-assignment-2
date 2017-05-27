def pairSum(_list, n):
    if len(_list) < 2:
        return
    integer_pairs = []
    pair_sum = 0
    for i in _list:
        for j in _list[1:]:
            pair_sum = i + j
            if pair_sum == n:
                integer_pairs.append([i,j])
    return integer_pairs
