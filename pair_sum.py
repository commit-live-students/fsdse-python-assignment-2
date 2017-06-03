def pairSum(ls, psum):
    return [(x, y) for i, x in enumerate(ls) for y in ls[i+1:] if x+y == psum]

print pairSum([2,3,4,10,7, 1, 9,6], 10)
