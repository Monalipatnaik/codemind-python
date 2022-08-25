n=int(input())
num=n
k=str(n)
l=len(k)
sum=0
while n>0:
    r=n%10
    sum=sum+r**l
    n=n//10
    l-=1
if sum==num:
    print(True)
else:
    print(False)