def pairSum(list_int, number):
    pair_sum = []
    for elem in range(len(list_int)):
        for elem1 in range(len(list_int)):
            sum = list_int[elem] + list_int[elem1]
            if (sum == number):
                result_numbers = list_int[elem], list_int[elem1]
                pair_sum.append(result_numbers)
    return pair_sum

pairSum([1, 2, 3, 4], 4)
