n,m=map(int,input().split())
while n!=m:
    if n>m:
        n=n-m
    elif m>n:
        m=m-n
print(n)