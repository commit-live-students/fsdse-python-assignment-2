def pairSum(l,s):
   if len(l) > 2:
       pair = ()
       list_of_pairs = []
       list_num = len(l)
       for i in range(list_num):
           for j in range(i + 1,list_num):
               if(l[i] + l[j] == s):
                   pair = (l[i],l[j])
                   list_of_pairs.append(pair)
       return list_of_pairs

list_num = [1,2,3,4]
sum_num = 5
print pairSum(list_num,sum_num)
