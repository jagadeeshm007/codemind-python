a,b=map(int,input().split())
##print(a,b)
if a<10 and b<10:
    if (a==b-1 and b==a+1) or (a==b+1 and b==a-1) :
        print("Yes")
    else:
        print("No")
else:
    if (a==10 and b==1) or (a==1 and b==10):
        print("Yes")
    else:
        print("No")