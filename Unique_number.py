n=int(input())
k=str(n)
k=list(k)
f=0
for i in k:
    if k.count(i)>1:
        f=1
if f==1:
    print("Not Unique Number")
else:
    print("Unique Number")