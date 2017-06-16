li = [1,2,3,4,4,3]
no = 5
def pairSum(l,number):
    ans = []
    for i in range(len(l)):
        a = len(l)
        while(a!=i):
            a=a-1
            if(l[a]+l[i]==number):
                ans.append((l[i],l[a]))
    s = {ans[0]}
    for i in range(1,len(ans)):
        s.add(ans[i])
    return s
s= pairSum(li,no)
print(s)
