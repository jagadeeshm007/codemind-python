def hdf(a,b):
    while a!=b:
        if a>b:
            a=a-b
        if b>a:
            b=b-a
    return a
n,m=map(int,input().split())
print((n*m)//hdf(n,m))