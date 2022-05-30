def pal(e):
    a=e
    t=k=0
    while a:
        t=a%10
        k=(k*10)+t
        a=a//10
    return k
t=int(input())
k=0
if t<0:
    k=1
    t=abs(t)
j=pal(t)
if k==1:
    print("-%d"%j)
else:
    print(j)