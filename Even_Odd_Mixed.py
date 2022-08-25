n=int(input())
e,c,o,m=0,0,0,0
while n>0:
    r=n%10
    if r%2==0:
        e+=1
    elif r%2!=0:
        o+=1
    else:
        m+=1
    c+=1
    n=n//10
if e==c:
    print("Even")
elif o==c:
    print("Odd")
else:
    print("Mixed")