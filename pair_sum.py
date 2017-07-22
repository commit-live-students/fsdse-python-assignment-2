def pairSum(a, b):
	for i in a:
		for j in range(len(a)):
			lst = []
			if (i + a[j]) == b:
				m =(i, a[j])
				lst.append(m)
				return lst
				
