n=input()
k=0
for i in n:
    if i.isdigit()==True:
        k+=1
if k>0:
    print("Contains %d digit"%k)
else:
    print("Doesn't contain digit")