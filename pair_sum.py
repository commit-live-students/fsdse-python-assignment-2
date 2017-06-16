def pairSum(li,n):
    a=[]
    for i in range(len(li)):
          for j in range(i+1, len(li)):
              if((li[i]+li[j]) == n):
                a.append((li[i], li[j]))
    return a
#a=pairSum([2, 5, 4, 3, 8, 7, 6, 1, 10, -1],9)
#print a
