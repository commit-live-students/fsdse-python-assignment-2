def pairSum(ls,num):
    final_list = []
    first = 0
    last = len(ls)-1
    while(first < last):
        if(ls[first]+ ls[last] == num):
            final_list.append((ls[first], ls[last]))
            first+=1
            last-=1
        elif (ls[first]+ls[last] < num):
            first+=1
        else:
            last-=1
    return final_list
