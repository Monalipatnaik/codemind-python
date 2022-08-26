n=int(input())
k=0
num=n
for i in range(1,n):
    if i*(i+1)==num:
        k+=1
        break
if k==1:
    print("YES")
else:
    print("NO")