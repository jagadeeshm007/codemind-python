def pal(a):
    k=t=0
    while a:
        t=a%10
        k=(k*10)+t
        a=a//10
    return k
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if i==pal(i):
        print(i,end=" ")