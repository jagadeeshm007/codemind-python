t=int(input())
while t:
    c=k=0
    a,b=map(int,input().split())
    for i in range(b):
        if (i**2)%b==a:
            k=1
            c=i
            break
    if k==1:
        print(c)
    else:
        print("-1")
    t-=1