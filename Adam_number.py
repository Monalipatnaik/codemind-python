n=int(input())
s1=n**2
st=str(n)
rev=st[::-1]
rev=int(rev)
s2=rev**2
s2=str(s2)
res=s2[::-1]
res=int(res)
if res==s1:
    print(True)
else:
    print(False)