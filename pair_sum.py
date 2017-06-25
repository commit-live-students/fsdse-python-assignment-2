def pairSum(ls, sum):
    return [(x, y) for i, x in enumerate(ls) for y in ls[i+1:] if x+y == sum]

print(pairSum([1,2,3,4,5,6,7,8,9],9))
