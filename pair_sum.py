def pairSum(lista,num1):
    final_list = []
    lista.sort()
    lower = 0
    upper = len(lista) - 1
    while lower < upper:
        if lista[lower] + lista [upper] == num1:
            lower +=1
            upper -=1
            final_list.append((lista[lower],lista[upper]))
        elif lista[lower] + lista [upper] < num1:
             lower +=1
        else:
            upper -=1
    return final_list
