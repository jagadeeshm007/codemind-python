def fac(a):
    m=1
    for i in range(1,a+1):
        m=m*i
    return m
n=int(input())
while n:
    t=int(input())
    print(fac(t))
    n-=1