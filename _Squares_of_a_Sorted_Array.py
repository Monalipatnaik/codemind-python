n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    r.append(i**2)
r=sorted(r)
print(*r)