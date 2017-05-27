def pairSum(given_list,given_sum):
    length = len(given_list)
    return_list = []
    for i in range(0,length-1):
        cal_sum = given_list[i] + given_list[i+1]
        if (cal_sum == given_sum):
            return_list.append(given_list[i])
            return_list.append(given_list[i+1])
        return return_list
        
pairSum([2, 5, 4, 3, 8, 7, 6, 1, 10, -1], 9)
