n=int(input())
l=list(map(int,input().split()))
k=int(input())
r=[]
for i in range(len(l)):
    if l[i]==k:
        r.append(i)
if len(r)==0:
    print("-1 -1")
else:
    print(r[0],r[len(r)-1])