def pairSum(l, num):
    if len(l) < 2:
        print("Enter a list of atleast two numbers")
        return 1
    for i in l:
        if type(i) != int:
            print("list should only contain integers")
            return 2
    new_l = []

    for num1 in l:
        all = [num2 for num2 in l if((num1 + num2) == num)]
        for num2 in all:
            new_l.append([num1,num2])

    return new_l
