def pairSum(b,n):
	y = []

	for i in range(len(b)):
   		for j in range(i+1,len(b)):
			sum = b[i]+b[j]
			if sum == n:
				y.append((b[i],b[j]))
	return y


print pairSum([1,2,3,4],5)
