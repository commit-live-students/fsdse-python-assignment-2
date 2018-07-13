def pairSum(x,y):
    if len(x)<2: return "Please enter two or more elements in list"
    lst = []
    for i in x:
        for j in x:
          if i+j==y:
              lst.append([i,j])
    return lst


print pairSum([1,2,3,4],5)
