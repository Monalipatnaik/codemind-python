t=int(input())
for i in range(t):
    k=0
    n=input()
    for i in n:
        if i.isdigit()==True:
            k+=1
    if k==0:
        print("No")
    else:
        print("Yes")