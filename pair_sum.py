def pairSum(input_list, sum):
    sum_pairs = []
    while len(input_list):
        a = input_list.pop(0)
        for i in input_list:
            if a + i == sum:
                sum_pairs.append([a, i])
                input_list.remove(i)
                break
    return sum_pairs
