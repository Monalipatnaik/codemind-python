n=input()
k=input()
l=0
for i in n:
    v=n.count(k)
    l+=1
    break
if v==0:
    print("-1")
else:
    print(v)