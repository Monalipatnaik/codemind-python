h,sp,se=map(int,input().split())
if h>50 and sp>60 and se>100:
    print("10")
elif h>50 and sp>60:
    print("9")
elif se>100 and sp>60:
    print("8")
elif h>50 and se>100:
    print("7")
elif h>50 or sp>60 or se>100:
    print("6")
else:
    print("5")