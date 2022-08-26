n=input()
sum=0
for i in n:
    if i.isdigit()==True:
        i=int(i)
        sum=sum+i
print(sum)