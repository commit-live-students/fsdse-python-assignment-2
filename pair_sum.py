def pairSum(n, number):
    if isinstance(n, list):
        if len(n) < 2:
            return False
        pair = []
        i = 0
        for i in range(i, len(n)+1):
            for j in range(i+1, len(n)+1):
                if number == (i + j):
                    pair.append((i,j))
        return pair


    else:
        return False
print pairSum([1,2,3,4,6,7,8,9,10],15)
