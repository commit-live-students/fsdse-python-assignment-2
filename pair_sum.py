def pairSum(lst1,num1):
    final_list = []
    lst1.sort()
    lower = 0
    upper = len(lst1) - 1
    while lower < upper:
        if lst1[lower] + lst1 [upper] == num1:
            lower +=1
            upper -=1
            final_list.append((lst1[lower],lst1[upper]))
        elif lst1[lower] + lst1 [upper] < num1:
             lower +=1
        else:
            upper -=1
    return final_list
