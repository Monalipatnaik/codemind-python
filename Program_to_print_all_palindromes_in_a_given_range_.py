def palindrome(n):
    num=n
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    if rev==num:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if palindrome(i)==True:
        print(i,end=" ")
        