t=int(input())
for i in range(t):
    n=input()
    k=0
    for i in n:
        if i.isdigit()==False:
            k+=1
    if k>0:
        print("False")
    else:
        print(True)