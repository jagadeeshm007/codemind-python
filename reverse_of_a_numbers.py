def rev(a):
    t=k=0
    while a:
        t=a%10
        k=(k*10)+t
        a=a//10
    return k
n=int(input())
print(rev(n))