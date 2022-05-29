def sum(n):
    t=s=0
    while n:
        t=n%10
        s=s+t
        n=n//10
    return s
n=int(input())
c=1
while c:
    if sum(n)<10:
        n=sum(n)
        c=0
        break
    else:
        n=sum(n)
print(n)