def factorial(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    return pro
n=int(input())
num=n
sum=0
while n>0:
    r=n%10
    k=factorial(r)
    sum=sum+k
    n=n//10
if sum==num:
    print("The number %d is a strong number"%num)
else:
    print("The number %d is not a strong number"%num)