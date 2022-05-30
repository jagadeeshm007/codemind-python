def pal(e):
    a=e
    t=k=0
    while a:
        t=a%10
        k=(k*10)+t
        a=a//10
    if e==k:
        return 1
    return 0
t=int(input())
while t:
    n=int(input())
    if pal(n)==1:
        print("True")
    else:
        print("False")
    t-=1