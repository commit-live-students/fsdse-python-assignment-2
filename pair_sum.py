def pairSum(arg_list, arg_num):
    output = []
    for x in arg_list:
        for n in arg_list:
            if x + n == arg_num:
                output.append((x, n))
    return output
