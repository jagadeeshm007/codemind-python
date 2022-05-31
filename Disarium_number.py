def rev(n):
    k=s=0
    while n:
        k=n%10
        s=(s*10)+k
        n=n//10
    return s
n=int(input())
k=rev(n)
t=m=0
i=1
while k:
    t=k%10
    m=m+(t**i)
    i+=1
    k=k//10
if m==n:
    print("True")
else:
    print("False")