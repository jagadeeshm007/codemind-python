def pretty(a):
    if a%10==2 or a%10==3 or a%10==9:
        return 1
    return 0
t=int(input())
while t:
    n,m=map(int,input().split())
    c=0
    if n<2:
        n=2
    for i in range(n,m+1):
        if pretty(i)==1:
            c+=1
    print(c)
    t-=1