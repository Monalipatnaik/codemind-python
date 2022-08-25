n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    k=str(i)
    le=len(k)
    if le%2==0:
        c+=1
print(c)